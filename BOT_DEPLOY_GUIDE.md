# 🤖 Telegram Bot Worker Deployment Guide

## ❌ Problem: Bot Not Responding

Backend healthy hai but bot respond nahi kar raha? 

**Reason:** Bot worker service alag se deploy karna padega!

---

## ✅ Solution: Separate Bot Service Deploy Karo

### Step 1: Koyeb me New Service Create Karo

1. Koyeb Dashboard me jao
2. **Create App** click karo
3. **GitHub** select karo
4. Same repository select karo: `chetanmehar590-oss/Ludomlehar277`

### Step 2: Service Configuration

**Service Name:** `ludo-bot-worker`

**Build Settings:**
- Builder: **Buildpack**
- Branch: `main`
- Build command: Leave EMPTY
- **Run command:** 
  ```bash
  python bot_main.py
  ```

**Instance:**
- Type: **Nano** (Free)
- Region: Same as backend (Singapore recommended)
- Scaling: Min=1, Max=1

### Step 3: Environment Variables (IMPORTANT!)

Bot ko same environment variables chaiye:

```bash
MONGO_URL = mongodb+srv://username:password@cluster.mongodb.net/
DB_NAME = ludo_club_db
TELEGRAM_BOT_TOKEN = 1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
WEB_APP_URL = https://your-frontend-url.koyeb.app
```

**Note:** `WEB_APP_URL` me aapka frontend ka URL dalna hai (baad me update kar lena)

### Step 4: Advanced Settings

**Health Checks:** 
- ⚠️ **DISABLE kar do!**
- Bot worker HTTP endpoint expose nahi karta
- Health check toggle ko **OFF** kar do

**Ports:**
- No port needed (bot worker doesn't serve HTTP)

### Step 5: Deploy

Click **Deploy** button aur wait karo 2-3 minutes.

---

## 🔍 Check Bot is Running

### Check Koyeb Logs

1. Bot service open karo
2. **Logs** tab click karo
3. Ye logs dikhne chahiye:

```
✅ 🤖 Starting Deep Night Ludo Club Telegram Bot...
✅ 📦 Environment:
   - BOT_TOKEN: 1234567890:ABCdef...
   - WEB_APP_URL: https://your-app.com
   - DB_NAME: ludo_club_db
✅ Bot application created successfully
✅ Starting bot with polling...
✅ Bot is running!
```

### Test in Telegram

1. Telegram me apne bot ko open karo
2. `/start` command bhejo
3. Bot should respond:
   ```
   🎲 Welcome to Deep Night Ludo Club Bot!
   
   To use this bot:
   1. Add me to your Ludo gaming group
   2. Use /start command in the group
   3. Click 'Place New Table' button to book your table
   
   📱 The booking form will open inside Telegram!
   ```

---

## 🎯 Complete Architecture

Aapko **3 services** chaiye:

### Service 1: Backend (Web API)
- **Name:** `ludo-backend`
- **Run:** `python main.py`
- **Port:** 8000
- **URL:** `https://ludo-backend-xxxxx.koyeb.app`

### Service 2: Bot Worker
- **Name:** `ludo-bot-worker`
- **Run:** `python bot_main.py`
- **Port:** None (no HTTP)
- **Health Check:** Disabled

### Service 3: Frontend (Optional)
- **Name:** `ludo-frontend`
- **Run:** `npx serve -s frontend/build -l $PORT`
- **Port:** 3000
- **URL:** `https://ludo-frontend-xxxxx.koyeb.app`

---

## 🧪 Test Bot Commands

Private chat me test karo:

### Test 1: /start
```
/start
```
Bot should send welcome message.

### Test 2: /help
```
/help
```
Bot should show help text.

### Test 3: In Group

1. Bot ko group me add karo
2. `/start` command group me bhejo
3. Bot should send **"Place New Table"** button
4. Button click karo → Web app should open

---

## ❌ Common Issues

### Issue 1: Bot Not Responding

**Symptoms:** No response in Telegram

**Check:**
```bash
# Check bot logs in Koyeb
# Look for:
❌ TELEGRAM_BOT_TOKEN not found
❌ Connection error
❌ Bot stopped
```

**Fix:**
- Verify `TELEGRAM_BOT_TOKEN` is set correctly
- Check token with @BotFather (`/mybots` → API Token)
- Redeploy bot service

### Issue 2: "Application exited with code 1"

**Symptoms:** Bot service unhealthy

**Fix:**
1. Check if all environment variables are set
2. Disable health checks
3. Check logs for specific error
4. Make sure `bot_main.py` exists in repo

### Issue 3: Button Not Appearing

**Symptoms:** Bot responds but no button in group

**Fix:**
1. Check bot has permission to send messages in group
2. Verify bot is not restricted
3. Use `/table` command explicitly

### Issue 4: Web App Not Opening

**Symptoms:** Button appears but clicking does nothing

**Fix:**
1. Check `WEB_APP_URL` is set correctly
2. URL must be HTTPS (not HTTP)
3. Configure domain in @BotFather:
   ```
   /mybots → Select bot → Edit Bot → Edit Web App
   → Enter your WEB_APP_URL
   ```

---

## 🔧 Bot Configuration in @BotFather

### Set Domain for Web App

```
/mybots
[Select your bot]
/setdomain
[Enter: https://your-frontend-url.koyeb.app]
```

### Set Commands

```
/mybots
[Select your bot]
/setcommands

start - Get started and show table button
help - Show help message
table - Send 'Place New Table' button
```

### Set Description

```
/mybots
[Select your bot]
/setdescription

Deep Night Ludo Club - Book your gaming tables easily!
```

---

## 📊 Service Status Check

All 3 services should be:

| Service | Status | URL |
|---------|--------|-----|
| Backend | ✅ Healthy | https://backend-xxx.koyeb.app |
| Bot Worker | ✅ Running | No URL (worker) |
| Frontend | ✅ Healthy | https://frontend-xxx.koyeb.app |

---

## 🚀 Quick Deploy Commands

### Push to GitHub
```bash
git add .
git commit -m "Add bot worker support"
git push origin main
```

### Create Bot Service in Koyeb

**Name:** `ludo-bot-worker`

**Run command:**
```bash
python bot_main.py
```

**Environment Variables:**
```bash
MONGO_URL=mongodb+srv://...
DB_NAME=ludo_club_db
TELEGRAM_BOT_TOKEN=your_token
WEB_APP_URL=https://your-frontend-url
```

**Advanced:**
- Health checks: OFF
- Scaling: 1-1

**Deploy!** ✅

---

## ✅ Success Checklist

- [ ] Backend service deployed and healthy
- [ ] Bot worker service deployed
- [ ] All environment variables set
- [ ] Bot responding to `/start` in private chat
- [ ] Bot sending button in group
- [ ] Button opens web app
- [ ] Web app loads correctly
- [ ] Form submission works

---

## 📞 Still Not Working?

### Check These:

1. **Bot Token Valid?**
   - @BotFather → /mybots → API Token
   - Copy exact token (no extra spaces)

2. **Bot Not Blocked?**
   - Check if you blocked the bot
   - Try `/unblock` or delete and re-add

3. **Bot Has Permissions?**
   - Bot can send messages in group?
   - Bot is not restricted?

4. **Logs Show Errors?**
   - Koyeb → Bot Service → Logs
   - Look for red error messages

---

**Bot ab kaam karega! 🤖✅**
