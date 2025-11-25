"""
Telegram Bot Worker Entry Point
This runs the bot separately from the web server
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

if __name__ == "__main__":
    print("=" * 60)
    print("🤖 Starting Deep Night Ludo Club Telegram Bot...")
    print("=" * 60)
    print(f"📦 Environment Check:")
    print(f"   - TELEGRAM_BOT_TOKEN: {'✅ SET' if os.environ.get('TELEGRAM_BOT_TOKEN') else '❌ NOT SET'}")
    print(f"   - WEB_APP_URL: {os.environ.get('WEB_APP_URL', '❌ NOT SET')}")
    print(f"   - DB_NAME: {os.environ.get('DB_NAME', '❌ NOT SET')}")
    print(f"   - MONGO_URL: {'✅ SET' if os.environ.get('MONGO_URL') else '❌ NOT SET'}")
    print("=" * 60)
    
    # Check if bot token exists
    if not os.environ.get('TELEGRAM_BOT_TOKEN'):
        print("❌ ERROR: TELEGRAM_BOT_TOKEN is not set!")
        print("Please set TELEGRAM_BOT_TOKEN environment variable.")
        sys.exit(1)
    
    # Import and run bot
    import asyncio
    
    try:
        # Import from backend
        sys.path.insert(0, str(current_dir / 'backend'))
        from telegram_bot import start_bot, stop_bot
        
        print("✅ Bot modules imported successfully")
        print("🚀 Starting bot polling...")
        
        async def run():
            app = await start_bot()
            if app:
                try:
                    await asyncio.Event().wait()
                except KeyboardInterrupt:
                    await stop_bot(app)
        
        asyncio.run(run())
        
    except KeyboardInterrupt:
        print("\n🛑 Bot stopped by user")
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Make sure backend/telegram_bot.py exists")
        import traceback
        traceback.print_exc()
    except Exception as e:
        print(f"❌ Bot error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
