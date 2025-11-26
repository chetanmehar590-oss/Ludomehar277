import os
import logging
from telegram import Update, WebAppInfo, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get environment variables
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
WEB_APP_URL = os.environ.get('WEB_APP_URL', 'https://your-app-url.com')

if not TELEGRAM_BOT_TOKEN:
    logger.warning("TELEGRAM_BOT_TOKEN not found in environment variables!")
    logger.warning("Bot will not start. Please set TELEGRAM_BOT_TOKEN in environment.")
    # Don't raise error, just log warning so backend can still start


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    user = update.effective_user
    chat_type = update.effective_chat.type
    
    if chat_type in ['group', 'supergroup']:
        # If in a group, send the Place New Table button and pin it
        message = await send_table_button(update, context)
        
        # Try to pin the message (needs admin rights)
        try:
            if message:
                await context.bot.pin_chat_message(
                    chat_id=update.effective_chat.id,
                    message_id=message.message_id,
                    disable_notification=True  # Silent pin
                )
                logger.info(f"Message pinned in chat: {update.effective_chat.id}")
        except Exception as e:
            logger.warning(f"Could not pin message: {e}")
            # Bot needs to be admin to pin messages
    else:
        # If in private chat, send welcome message
        welcome_message = (
            f"🎲 Welcome to Deep Night Ludo Club Bot, {user.first_name}!\n\n"
            "To use this bot:\n"
            "1. Add me to your Ludo gaming group\n"
            "2. Make me admin (so I can pin messages)\n"
            "3. Use /start command in the group\n"
            "4. I'll send and pin the 'Place New Table' button\n\n"
            "📱 The booking form will open inside Telegram!"
        )
        await update.message.reply_text(welcome_message)


async def send_table_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send 'Place New Table' button in group"""
    # Use simple URL button instead of WebApp (more reliable)
    keyboard = [
        [
            InlineKeyboardButton(
                "🎲 Place New Table",
                url=WEB_APP_URL
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    message = (
        "🎮 **Deep Night Ludo Club**\n\n"
        "Click the button below to place your table request:\n"
        "💰 Amount | 🎲 Type | 📊 Game+ | ⚙️ Options\n\n"
        "👇 Book your table now!"
    )
    
    sent_message = await update.message.reply_text(
        message,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )
    logger.info(f"Table button sent to chat: {update.effective_chat.id}")
    
    return sent_message  # Return message object for pinning


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command"""
    help_text = (
        "🎲 **Deep Night Ludo Club Bot - Help**\n\n"
        "**Available Commands:**\n"
        "/start - Get started and show table button\n"
        "/help - Show this help message\n"
        "/table - Send 'Place New Table' button\n\n"
        "**How to use:**\n"
        "1. Use /start or /table command in your group\n"
        "2. Click 'Place New Table' button\n"
        "3. Fill in the booking form\n"
        "4. Submit your table request\n\n"
        "💡 The form opens inside Telegram as a Mini App!"
    )
    await update.message.reply_text(help_text, parse_mode='Markdown')


async def table_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /table command - same as start in groups"""
    await send_table_button(update, context)


async def handle_group_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle messages in groups (optional)"""
    # You can add logic here to handle specific messages
    # For example, if someone types 'table' or 'book'
    message_text = update.message.text.lower() if update.message.text else ''
    
    if 'table' in message_text or 'book' in message_text:
        await send_table_button(update, context)


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle errors"""
    logger.error(f"Update {update} caused error {context.error}")


def create_bot_application():
    """Create and configure the bot application"""
    if not TELEGRAM_BOT_TOKEN:
        logger.warning("Cannot create bot application without token")
        return None
    
    # Create application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Add command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("table", table_command))
    
    # Add message handler for groups (optional)
    # application.add_handler(
    #     MessageHandler(
    #         filters.TEXT & filters.ChatType.GROUPS,
    #         handle_group_message
    #     )
    # )
    
    # Add error handler
    application.add_error_handler(error_handler)
    
    logger.info("Bot application created successfully")
    return application


async def start_bot():
    """Start the bot with polling"""
    application = create_bot_application()
    
    if application:
        logger.info("Starting bot with polling...")
        await application.initialize()
        await application.start()
        await application.updater.start_polling()
        logger.info("Bot is running!")
        return application
    else:
        logger.error("Failed to start bot - no token provided")
        return None


async def stop_bot(application):
    """Stop the bot gracefully"""
    if application:
        logger.info("Stopping bot...")
        await application.updater.stop()
        await application.stop()
        await application.shutdown()
        logger.info("Bot stopped")


if __name__ == "__main__":
    import asyncio
    
    async def main():
        app = await start_bot()
        if app:
            # Keep the bot running
            try:
                # Run forever
                await asyncio.Event().wait()
            except KeyboardInterrupt:
                await stop_bot(app)
    
    asyncio.run(main())
