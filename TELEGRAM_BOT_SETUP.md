# 🤖 Deep Night Ludo Club - Telegram Bot Setup Guide

## 📋 Prerequisites

1. **Telegram Bot Token**
   - Open Telegram and search for [@BotFather](https://t.me/botfather)
   - Send `/newbot` command
   - Follow the instructions to create your bot
   - Copy the Bot Token (format: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`)

2. **Deployed Web App URL**
   - Your web app must be hosted with HTTPS
   - Telegram Mini Apps require HTTPS (HTTP won't work)
   - Options:
     - Deploy on Emergent (recommended)
     - Use ngrok for local development
     - Deploy on Vercel, Netlify, Railway, etc.

## 🔧 Configuration

### Step 1: Set Environment Variables

Edit `/app/backend/.env` file and add:

```bash
# Telegram Bot Token (from BotFather)
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz

# Your deployed web app URL (must be HTTPS)
WEB_APP_URL=https://your-app-url.com
```

### Step 2: Configure Bot with BotFather

In Telegram, send these commands to @BotFather:

```
/mybots
[Select your bot]
/setdomain
[Enter your WEB_APP_URL]
```

This tells Telegram that your bot can use Web Apps.

### Step 3: Set Bot Commands (Optional)

To show commands in the bot menu:

```
/mybots
[Select your bot]
/setcommands

Then paste:
start - Get started and show table button
help - Show help message
table - Send 'Place New Table' button
```

## 🚀 Running the Bot

### Option 1: Run Standalone Bot

```bash
cd /app/backend
python bot_runner.py
```

This will start the bot in polling mode.

### Option 2: Run with FastAPI Server

The bot is integrated with the FastAPI server and will start automatically when the server runs.

```bash
cd /app/backend
sudo supervisorctl restart backend
```

## 📱 How to Use

### In Groups:

1. Add your bot to a Telegram group
2. Make sure the bot has permission to send messages
3. In the group, type `/start` or `/table`
4. Bot will send a "🎲 Place New Table" button
5. Click the button to open the booking form inside Telegram
6. Fill the form and submit

### In Private Chat:

1. Open your bot in Telegram
2. Send `/start`
3. Bot will explain how to use it

## 🔍 Bot Commands

- `/start` - Welcome message (in private) or send table button (in groups)
- `/help` - Show help information
- `/table` - Send "Place New Table" button in groups

## 🛠️ Troubleshooting

### Bot Not Responding?

1. Check if bot is running: `ps aux | grep bot_runner`
2. Check logs: `tail -f /var/log/supervisor/backend.*.log`
3. Verify `TELEGRAM_BOT_TOKEN` is set correctly
4. Make sure bot is not blocked in the group

### Button Not Opening Web App?

1. Verify `WEB_APP_URL` is HTTPS (not HTTP)
2. Make sure domain is configured in BotFather
3. Check if URL is accessible from browser
4. Try restarting the bot

### Web App Not Loading?

1. Check CORS settings in backend
2. Verify app is deployed and accessible
3. Check browser console for errors
4. Make sure Telegram can reach your URL

## 🌐 Local Development with ngrok

For testing locally:

```bash
# Install ngrok
# Start your app on localhost:3000

# In another terminal:
ngrok http 3000

# Copy the HTTPS URL (e.g., https://abc123.ngrok.io)
# Update WEB_APP_URL in .env
WEB_APP_URL=https://abc123.ngrok.io

# Restart the bot
```

## 📝 Important Notes

- **HTTPS Required**: Telegram Mini Apps only work with HTTPS URLs
- **Bot Token Security**: Never commit your bot token to GitHub
- **Group Permissions**: Bot needs send message permission in groups
- **Rate Limits**: Telegram has rate limits for bots, don't spam

## 🎯 Features

✅ Send "Place New Table" button in groups
✅ Web App opens inside Telegram (Mini App)
✅ All booking features work in Telegram
✅ No need to leave Telegram
✅ Works on mobile and desktop

## 📞 Support

If you face any issues:
1. Check the logs
2. Verify all environment variables
3. Test the web app URL in browser
4. Check bot permissions in group

---

**Happy Gaming! 🎲🎮**
