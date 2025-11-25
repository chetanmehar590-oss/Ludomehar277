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
    print("🤖 Starting Deep Night Ludo Club Telegram Bot...")
    print(f"📦 Environment:")
    print(f"   - BOT_TOKEN: {os.environ.get('TELEGRAM_BOT_TOKEN', 'NOT SET')[:20]}...")
    print(f"   - WEB_APP_URL: {os.environ.get('WEB_APP_URL', 'NOT SET')}")
    print(f"   - DB_NAME: {os.environ.get('DB_NAME', 'NOT SET')}")
    
    # Import and run bot
    from backend.bot_runner import main
    import asyncio
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 Bot stopped by user")
    except Exception as e:
        print(f"❌ Bot error: {e}")
        import traceback
        traceback.print_exc()
