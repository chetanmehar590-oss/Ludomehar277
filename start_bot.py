#!/usr/bin/env python3
"""
Simple bot starter - Alternative to bot_main.py
This is simpler and should work without import issues
"""
import os
import sys
import asyncio
from pathlib import Path

# Add backend directory to Python path
backend_dir = Path(__file__).parent / 'backend'
sys.path.insert(0, str(backend_dir))
sys.path.insert(0, str(Path(__file__).parent))

print("=" * 60)
print("🤖 Deep Night Ludo Club - Telegram Bot Starter")
print("=" * 60)

# Check environment variables
required_vars = ['TELEGRAM_BOT_TOKEN', 'WEB_APP_URL', 'DB_NAME', 'MONGO_URL']
missing_vars = []

for var in required_vars:
    value = os.environ.get(var)
    if value:
        # Mask sensitive values
        if 'TOKEN' in var:
            display = value[:15] + "..." if len(value) > 15 else "SET"
        elif 'MONGO' in var:
            display = value[:30] + "..." if len(value) > 30 else "SET"
        else:
            display = value
        print(f"✅ {var}: {display}")
    else:
        print(f"❌ {var}: NOT SET")
        missing_vars.append(var)

print("=" * 60)

if missing_vars:
    print(f"❌ Missing environment variables: {', '.join(missing_vars)}")
    print("Please set these variables in Koyeb dashboard")
    sys.exit(1)

print("📦 Importing bot modules...")

try:
    # Direct import from telegram_bot
    import telegram_bot
    
    print("✅ telegram_bot module imported")
    print("🚀 Starting bot...")
    
    async def main():
        app = await telegram_bot.start_bot()
        if app:
            print("✅ Bot is running and listening for updates!")
            print("Press Ctrl+C to stop")
            try:
                await asyncio.Event().wait()
            except KeyboardInterrupt:
                print("\n🛑 Stopping bot...")
                await telegram_bot.stop_bot(app)
                print("✅ Bot stopped")
        else:
            print("❌ Failed to start bot")
            sys.exit(1)
    
    # Run the bot
    asyncio.run(main())

except ImportError as e:
    print(f"❌ Import Error: {e}")
    print("\nTrying alternative import method...")
    
    try:
        # Try importing as module
        from backend import telegram_bot
        
        async def main():
            app = await telegram_bot.start_bot()
            if app:
                print("✅ Bot started with alternative import!")
                await asyncio.Event().wait()
            else:
                sys.exit(1)
        
        asyncio.run(main())
    except Exception as e2:
        print(f"❌ Alternative import also failed: {e2}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
