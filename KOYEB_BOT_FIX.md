# 🔧 Koyeb Bot Import Error Fix

## ❌ Error: ModuleNotFoundError: No module named 'telegram_bot'

Ye error import path ki wajah se aa raha tha.

## ✅ Solution: 2 Options

### Option 1: Use start_bot.py (Recommended - Simpler)

Koyeb me **Run command** change karo:

```bash
python start_bot.py
```

Ye file simpler hai aur import issues handle kar leti hai.

---

### Option 2: Use bot_main.py (Original)

Koyeb me **Run command**:

```bash
python bot_main.py
```

Maine import paths fix kar diye hain, ab ye bhi kaam karega.

---

## 🚀 Complete Steps (Fresh Deploy)

### Step 1: GitHub pe Push Karo

```bash
git add .
git commit -m "Fix bot import errors"
git push origin main
```

### Step 2: Koyeb me Service Settings

**Service:** `ludo-bot-worker`

**Run Command (Choose one):**
```bash
python start_bot.py
```
OR
```bash
python bot_main.py
```

### Step 3: Environment Variables (MUST HAVE!)

```
TELEGRAM_BOT_TOKEN = 8222802213:AAE-n9hBawD5D6EaZ82nt3vFWq6...
DB_NAME = ludo_club_db
MONGO_URL = mongodb+srv://Ludo:RpfS4DlD5eXvt4dz@cluster...
WEB_APP_URL = https://your-frontend-url.com
```

**Important:** Variable names exact hone chahiye! `BOT_TOKEN` nahi, `TELEGRAM_BOT_TOKEN`

### Step 4: Advanced Settings

- **Health checks:** OFF / Disabled
- **Ports:** None needed

### Step 5: Deploy

Click **"Save and deploy"**

---

## 🔍 Expected Logs (Success)

```
============================================================
🤖 Deep Night Ludo Club - Telegram Bot Starter
============================================================
✅ TELEGRAM_BOT_TOKEN: 8222802213:AAE...
✅ WEB_APP_URL: https://your-app.com
✅ DB_NAME: ludo_club_db
✅ MONGO_URL: mongodb+srv://...
============================================================
📦 Importing bot modules...
✅ telegram_bot module imported
🚀 Starting bot...
✅ Bot is running and listening for updates!
```

---

## ❌ If Still Error

### Check 1: All Variables Set?

In Koyeb environment section:
- ✅ TELEGRAM_BOT_TOKEN (NOT BOT_TOKEN)
- ✅ DB_NAME
- ✅ MONGO_URL
- ✅ WEB_APP_URL

### Check 2: Files Pushed to GitHub?

```bash
# Check if files exist
git ls-files | grep -E "(start_bot|bot_main|telegram_bot)"
```

Should show:
```
start_bot.py
bot_main.py
backend/telegram_bot.py
backend/bot_runner.py
```

### Check 3: Health Checks Disabled?

Bot worker doesn't need HTTP health checks.

---

## 🧪 Test Locally First

```bash
cd /app

# Set env vars
export TELEGRAM_BOT_TOKEN="your_token"
export WEB_APP_URL="https://example.com"
export DB_NAME="ludo_club_db"
export MONGO_URL="your_mongo_url"

# Test
python start_bot.py
```

If this works locally, it will work on Koyeb!

---

## 📞 Quick Checklist

Before deploying:

- [ ] Files pushed to GitHub
- [ ] Run command: `python start_bot.py`
- [ ] All 4 env vars set with correct names
- [ ] Health checks disabled
- [ ] No port configuration

---

## ✅ After Successful Deploy

1. **Check Logs:**
   - Service → Logs tab
   - Should see "Bot is running"

2. **Test in Telegram:**
   ```
   /start
   ```
   Bot should respond!

3. **Test in Group:**
   - Add bot to group
   - Send `/start`
   - Button should appear

---

**Most Common Mistake:** Using `BOT_TOKEN` instead of `TELEGRAM_BOT_TOKEN` ⚠️

Fix this and bot will work! 🤖✅
