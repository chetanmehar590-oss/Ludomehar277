from fastapi import FastAPI, APIRouter, HTTPException
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional
import uuid
from datetime import datetime, timezone


ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Create the main app without a prefix
app = FastAPI()

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")


# Define Models
class StatusCheck(BaseModel):
    model_config = ConfigDict(extra="ignore")  # Ignore MongoDB's _id field
    
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    client_name: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class StatusCheckCreate(BaseModel):
    client_name: str


# Table Booking Models
class TableRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")
    
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    user_id: Optional[str] = None
    amount: float
    type: str
    game_plus: int = 0
    options: List[str] = []
    status: str = "pending"  # pending, confirmed, completed, cancelled
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class TableRequestCreate(BaseModel):
    user_id: Optional[str] = None
    amount: float
    type: str
    game_plus: int = 0
    options: List[str] = []

class TableRequestUpdate(BaseModel):
    amount: Optional[float] = None
    type: Optional[str] = None
    game_plus: Optional[int] = None
    options: Optional[List[str]] = None
    status: Optional[str] = None

class UserBalance(BaseModel):
    model_config = ConfigDict(extra="ignore")
    
    user_id: str
    balance: float
    last_updated: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

# Add your routes to the router instead of directly to app
@api_router.get("/")
async def root():
    return {"message": "Hello World"}

@api_router.post("/status", response_model=StatusCheck)
async def create_status_check(input: StatusCheckCreate):
    status_dict = input.model_dump()
    status_obj = StatusCheck(**status_dict)
    
    # Convert to dict and serialize datetime to ISO string for MongoDB
    doc = status_obj.model_dump()
    doc['timestamp'] = doc['timestamp'].isoformat()
    
    _ = await db.status_checks.insert_one(doc)
    return status_obj

@api_router.get("/status", response_model=List[StatusCheck])
async def get_status_checks():
    # Exclude MongoDB's _id field from the query results
    status_checks = await db.status_checks.find({}, {"_id": 0}).to_list(1000)
    
    # Convert ISO string timestamps back to datetime objects
    for check in status_checks:
        if isinstance(check['timestamp'], str):
            check['timestamp'] = datetime.fromisoformat(check['timestamp'])
    
    return status_checks


# Table Request Endpoints
@api_router.post("/tables", response_model=TableRequest)
async def create_table_request(table: TableRequestCreate):
    """Create a new table request"""
    table_dict = table.model_dump()
    table_obj = TableRequest(**table_dict)
    
    # Convert to dict and serialize datetime
    doc = table_obj.model_dump()
    doc['timestamp'] = doc['timestamp'].isoformat()
    
    await db.table_requests.insert_one(doc)
    logger.info(f"Table request created: {table_obj.id}")
    return table_obj

@api_router.get("/tables", response_model=List[TableRequest])
async def get_table_requests(user_id: Optional[str] = None, status: Optional[str] = None):
    """Get all table requests with optional filters"""
    query = {}
    if user_id:
        query['user_id'] = user_id
    if status:
        query['status'] = status
    
    tables = await db.table_requests.find(query, {"_id": 0}).sort("timestamp", -1).to_list(1000)
    
    # Convert ISO string timestamps back to datetime
    for table in tables:
        if isinstance(table['timestamp'], str):
            table['timestamp'] = datetime.fromisoformat(table['timestamp'])
    
    return tables

@api_router.get("/tables/{table_id}", response_model=TableRequest)
async def get_table_request(table_id: str):
    """Get a specific table request by ID"""
    table = await db.table_requests.find_one({"id": table_id}, {"_id": 0})
    
    if not table:
        raise HTTPException(status_code=404, detail="Table request not found")
    
    if isinstance(table['timestamp'], str):
        table['timestamp'] = datetime.fromisoformat(table['timestamp'])
    
    return table

@api_router.put("/tables/{table_id}", response_model=TableRequest)
async def update_table_request(table_id: str, update: TableRequestUpdate):
    """Update a table request"""
    # Get existing table
    existing_table = await db.table_requests.find_one({"id": table_id}, {"_id": 0})
    
    if not existing_table:
        raise HTTPException(status_code=404, detail="Table request not found")
    
    # Update only provided fields
    update_data = {k: v for k, v in update.model_dump().items() if v is not None}
    
    if update_data:
        await db.table_requests.update_one(
            {"id": table_id},
            {"$set": update_data}
        )
    
    # Fetch updated table
    updated_table = await db.table_requests.find_one({"id": table_id}, {"_id": 0})
    
    if isinstance(updated_table['timestamp'], str):
        updated_table['timestamp'] = datetime.fromisoformat(updated_table['timestamp'])
    
    logger.info(f"Table request updated: {table_id}")
    return updated_table

@api_router.delete("/tables/{table_id}")
async def delete_table_request(table_id: str):
    """Delete a table request"""
    result = await db.table_requests.delete_one({"id": table_id})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Table request not found")
    
    logger.info(f"Table request deleted: {table_id}")
    return {"message": "Table request deleted successfully", "id": table_id}

@api_router.get("/tables/latest/{user_id}", response_model=TableRequest)
async def get_latest_table_request(user_id: str):
    """Get the latest table request for a user"""
    tables = await db.table_requests.find(
        {"user_id": user_id}, 
        {"_id": 0}
    ).sort("timestamp", -1).limit(1).to_list(1)
    
    if not tables:
        raise HTTPException(status_code=404, detail="No table requests found for this user")
    
    table = tables[0]
    if isinstance(table['timestamp'], str):
        table['timestamp'] = datetime.fromisoformat(table['timestamp'])
    
    return table


# User Balance Endpoints
@api_router.get("/user/balance/{user_id}")
async def get_user_balance(user_id: str):
    """Get user balance"""
    user = await db.users.find_one({"user_id": user_id}, {"_id": 0})
    
    if not user:
        # Return default balance for new users
        return {"user_id": user_id, "balance": 28.00}
    
    return {"user_id": user_id, "balance": user.get("balance", 28.00)}

@api_router.post("/user/balance/{user_id}")
async def update_user_balance(user_id: str, balance: float):
    """Update user balance"""
    result = await db.users.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "balance": balance,
                "last_updated": datetime.now(timezone.utc).isoformat()
            }
        },
        upsert=True
    )
    
    logger.info(f"Balance updated for user {user_id}: {balance}")
    return {"user_id": user_id, "balance": balance, "updated": True}


# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()