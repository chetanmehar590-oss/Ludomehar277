#!/usr/bin/env python3
"""
Telegram Bot Runner
Run this file to start the Telegram bot

Usage:
    python bot_runner.py
"""

import asyncio
import logging
import sys
from telegram_bot import start_bot, stop_bot

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def main():
    """Main function to run the bot"""
    logger.info("="*50)
    logger.info("Deep Night Ludo Club Telegram Bot")
    logger.info("="*50)
    
    try:
        # Start the bot
        app = await start_bot()
        
        if app:
            logger.info("Bot is running! Press Ctrl+C to stop.")
            logger.info("="*50)
            
            # Keep running until interrupted
            try:
                await asyncio.Event().wait()
            except KeyboardInterrupt:
                logger.info("\nShutdown signal received...")
                await stop_bot(app)
        else:
            logger.error("Failed to start bot. Please check your configuration.")
            logger.error("Make sure TELEGRAM_BOT_TOKEN is set in .env file")
            sys.exit(1)
            
    except Exception as e:
        logger.error(f"Error running bot: {e}")
        sys.exit(1)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
        sys.exit(0)
