#!/usr/bin/env python3
"""
Run both backend server and bot together
"""
import asyncio
import os
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent))

async def run_bot():
    """Run bot in background"""
    try:
        from backend.telegram_bot import start_bot
        print("🤖 Starting Telegram Bot...")
        bot_app = await start_bot()
        if bot_app:
            print("✅ Bot started successfully")
            # Keep bot running
            await asyncio.Event().wait()
    except Exception as e:
        print(f"⚠️ Bot error: {e}")

async def main():
    """Run both server and bot"""
    # Start bot in background
    bot_task = asyncio.create_task(run_bot())
    
    # Start FastAPI server
    import uvicorn
    from backend.server import app
    
    port = int(os.environ.get("PORT", 8001))
    
    print("🚀 Starting backend server...")
    config = uvicorn.Config(app, host="0.0.0.0", port=port, log_level="info")
    server = uvicorn.Server(config)
    
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())
