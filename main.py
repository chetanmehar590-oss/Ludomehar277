"""
Main entry point for Koyeb deployment
This file helps Koyeb detect Python app
"""
import sys
import os

# Add backend to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

# Import and run the app
if __name__ == "__main__":
    import uvicorn
    from backend.server import app
    
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
