#!/usr/bin/env python3
"""
Test script to verify environment variables
Run this before deploying to check configuration
"""
import os
import sys

def check_env():
    print("=" * 50)
    print("Environment Variables Check")
    print("=" * 50)
    
    required = {
        'MONGO_URL': 'MongoDB connection string',
        'DB_NAME': 'Database name',
        'TELEGRAM_BOT_TOKEN': 'Telegram bot token',
        'WEB_APP_URL': 'Frontend web app URL'
    }
    
    optional = {
        'PORT': 'Server port (default: 8000)',
        'CORS_ORIGINS': 'CORS origins (default: *)'
    }
    
    all_ok = True
    
    print("\n✅ Required Variables:")
    for var, desc in required.items():
        value = os.environ.get(var)
        if value:
            # Mask sensitive values
            if 'TOKEN' in var or 'PASSWORD' in var or 'URL' in var and 'mongodb' in value.lower():
                display = value[:20] + "..." if len(value) > 20 else value
            else:
                display = value
            print(f"   ✅ {var}: {display}")
        else:
            print(f"   ❌ {var}: NOT SET - {desc}")
            all_ok = False
    
    print("\n📋 Optional Variables:")
    for var, desc in optional.items():
        value = os.environ.get(var)
        if value:
            print(f"   ✅ {var}: {value}")
        else:
            print(f"   ⚠️  {var}: Not set (using default) - {desc}")
    
    print("\n" + "=" * 50)
    if all_ok:
        print("✅ All required environment variables are set!")
        print("You can proceed with deployment.")
        return 0
    else:
        print("❌ Some required variables are missing!")
        print("Please set them before deploying.")
        return 1

if __name__ == "__main__":
    sys.exit(check_env())
