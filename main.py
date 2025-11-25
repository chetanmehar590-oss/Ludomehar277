"""
Main entry point for Koyeb deployment
This file helps Koyeb detect Python app
"""
import sys
import os
from pathlib import Path

# Add current directory to Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

# Set default environment variables if not present
os.environ.setdefault('DB_NAME', 'ludo_club_db')
os.environ.setdefault('MONGO_URL', 'mongodb://localhost:27017/')
os.environ.setdefault('CORS_ORIGINS', '*')

# Import and run the app
if __name__ == "__main__":
    import uvicorn
    
    # Import after path is set
    from backend.server import app
    
    port = int(os.environ.get("PORT", 8000))
    
    print(f"🚀 Starting Deep Night Ludo Club on port {port}")
    print(f"📦 Environment:")
    print(f"   - DB_NAME: {os.environ.get('DB_NAME', 'not set')}")
    print(f"   - MONGO_URL: {os.environ.get('MONGO_URL', 'not set')[:30]}...")
    print(f"   - PORT: {port}")
    
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")
