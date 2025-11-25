# 🚀 Deep Night Ludo Club - Deployment Guide

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [Environment Setup](#environment-setup)
3. [GitHub Setup](#github-setup)
4. [Telegram Bot Configuration](#telegram-bot-configuration)
5. [Deployment Options](#deployment-options)
6. [Post-Deployment](#post-deployment)

---

## Prerequisites

Before deploying, make sure you have:

✅ **Telegram Bot Token** from [@BotFather](https://t.me/botfather)
✅ **MongoDB** database (local or cloud like MongoDB Atlas)
✅ **HTTPS URL** for your deployed app (required for Telegram Mini Apps)

---

## Environment Setup

### 1. Backend Environment Variables

Create `/app/backend/.env` file:

```bash
# MongoDB Configuration
MONGO_URL=mongodb://localhost:27017/
DB_NAME=ludo_club_db

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz

# Web App URL (HTTPS required!)
WEB_APP_URL=https://your-deployed-app-url.com

# CORS (Optional - for security)
CORS_ORIGINS=*
```

### 2. Frontend Environment Variables

Your `/app/frontend/.env` already has:

```bash
REACT_APP_BACKEND_URL=<your-backend-url>
```

This is automatically configured by the platform.

---

## GitHub Setup

### Option 1: Save via Emergent UI

1. Click on **Profile Icon** (top right)
2. Select **"Connect GitHub"**
3. Authorize Emergent to access your repositories
4. Click **"Save to GitHub"** button
5. Choose branch (or create new one)
6. Click **"PUSH TO GITHUB"**

### Option 2: Manual Git Push

```bash
# From /app directory
git add .
git commit -m "Deep Night Ludo Club - Complete with Telegram Bot"
git push origin main
```

**⚠️ Important:** Never commit your actual `.env` file! Only `.env.example` should be in Git.

---

## Telegram Bot Configuration

### Step 1: Create Bot with BotFather

1. Open Telegram and search for [@BotFather](https://t.me/botfather)
2. Send `/newbot` command
3. Follow instructions:
   - Choose bot name (e.g., "Deep Night Ludo Club Bot")
   - Choose username (e.g., "DeepNightLudoBot")
4. Copy the Bot Token you receive

### Step 2: Configure Bot Commands

Send to @BotFather:

```
/mybots
[Select your bot]
/setcommands

Then paste:
start - Get started and show table button
help - Show help message
table - Send 'Place New Table' button
```

### Step 3: Enable Web App

```
/mybots
[Select your bot]
/setdomain
[Enter your WEB_APP_URL]
```

This tells Telegram your bot can use Web Apps.

---

## Deployment Options

### Option A: Deploy on Emergent (Recommended)

1. Your app is already running on Emergent
2. Get your deployed URL from the platform
3. Update `WEB_APP_URL` in backend `.env`
4. Restart services:
   ```bash
   sudo supervisorctl restart all
   ```

### Option B: Deploy on Railway.app

1. Push code to GitHub
2. Go to [Railway.app](https://railway.app)
3. Create new project from GitHub repo
4. Add environment variables:
   - `MONGO_URL`
   - `DB_NAME`
   - `TELEGRAM_BOT_TOKEN`
   - `WEB_APP_URL`
5. Deploy!

### Option C: Deploy on Render.com

1. Push code to GitHub
2. Go to [Render.com](https://render.com)
3. Create Web Service for backend
4. Create Static Site for frontend
5. Add environment variables
6. Deploy both services

### Option D: Deploy on Vercel + Railway

**Frontend (Vercel):**
1. Push to GitHub
2. Import project to Vercel
3. Set `REACT_APP_BACKEND_URL`
4. Deploy

**Backend (Railway):**
1. Deploy backend to Railway
2. Add environment variables
3. Get backend URL and update frontend

---

## Post-Deployment

### 1. Update Environment Variables

After deployment, update `.env` with your actual URLs:

```bash
# Backend .env
WEB_APP_URL=https://your-actual-frontend-url.com
TELEGRAM_BOT_TOKEN=your_actual_token

# Frontend .env (usually auto-configured)
REACT_APP_BACKEND_URL=https://your-actual-backend-url.com
```

### 2. Start Telegram Bot

#### On Server:

```bash
cd /app/backend
python bot_runner.py &
```

#### Or with PM2 (recommended for production):

```bash
# Install PM2
npm install -g pm2

# Start bot
cd /app/backend
pm2 start bot_runner.py --name telegram-bot --interpreter python3

# Check status
pm2 status

# View logs
pm2 logs telegram-bot
```

### 3. Test the Bot

1. Add bot to a Telegram group
2. Send `/start` command
3. Click "Place New Table" button
4. Web app should open inside Telegram
5. Fill form and submit
6. Check if data is saved in MongoDB

### 4. Monitor Logs

```bash
# Backend logs
tail -f /var/log/supervisor/backend.*.log

# Bot logs (if using PM2)
pm2 logs telegram-bot

# MongoDB logs
tail -f /var/log/mongodb/mongod.log
```

---

## 🔒 Security Checklist

Before going live:

- [ ] Bot token is in `.env` (not hardcoded)
- [ ] `.env` is in `.gitignore`
- [ ] HTTPS is enabled for web app
- [ ] CORS is properly configured
- [ ] MongoDB connection string is secure
- [ ] Rate limiting is implemented (optional)
- [ ] Input validation is working

---

## 🐛 Troubleshooting

### Bot Not Responding?

```bash
# Check if bot process is running
ps aux | grep bot_runner

# Check bot logs
tail -f /var/log/supervisor/backend.*.log

# Restart bot
python bot_runner.py
```

### Web App Not Opening in Telegram?

1. Verify `WEB_APP_URL` is HTTPS (not HTTP)
2. Check if domain is set in @BotFather
3. Test URL in browser first
4. Clear Telegram cache

### Database Connection Issues?

```bash
# Test MongoDB connection
mongosh $MONGO_URL

# Check if MongoDB is running
sudo systemctl status mongod
```

### CORS Errors?

Update backend CORS settings in `server.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend-url.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 📞 Support Resources

- **Telegram Bot API Docs:** https://core.telegram.org/bots/api
- **Telegram Web Apps:** https://core.telegram.org/bots/webapps
- **FastAPI Docs:** https://fastapi.tiangolo.com
- **React Docs:** https://react.dev

---

## 🎉 You're All Set!

Your Deep Night Ludo Club Bot is now:

✅ Deployed and running
✅ Integrated with Telegram
✅ Connected to MongoDB
✅ Ready to accept table bookings!

**Happy Gaming! 🎲🎮**
