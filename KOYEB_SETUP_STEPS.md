# 🚀 Koyeb Deployment - Step by Step Fix

## ✅ Files Updated (Already Done)

Maine ye files create/update kar diye hain:
- ✅ `/main.py` - Root level entry point
- ✅ `/requirements.txt` - Root level dependencies
- ✅ `/Procfile` - Simplified run command
- ✅ `/koyeb.yaml` - Koyeb configuration

## 📤 Step 1: GitHub pe Push Karo

```bash
git add .
git commit -m "Fix Koyeb buildpack detection"
git push origin main
```

---

## 🔧 Step 2: Koyeb me Service Delete & Recreate Karo

### 2.1 Delete Old Service
1. Koyeb Dashboard me jao
2. Apni service select karo
3. **Settings** → Scroll down
4. **Delete Service** click karo

### 2.2 Create New Service - BACKEND

1. **Create App** click karo
2. **GitHub** select karo
3. Repository: `chetanmehar590-oss/Ludomlehar277` select karo
4. **Service Name**: `ludo-backend`

### 2.3 Configure Settings

**Build:**
- Builder: **Buildpack** (automatic detection)
- Branch: `main`
- Build command: Leave EMPTY (auto-detected)
- Run command: `python main.py`

**Instance:**
- Type: **Nano** (Free)
- Region: **Singapore** (sin)

**Environment Variables** (IMPORTANT!):
```
MONGO_URL = mongodb+srv://username:password@cluster.mongodb.net/
DB_NAME = ludo_club_db
TELEGRAM_BOT_TOKEN = 1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
WEB_APP_URL = https://your-frontend-url.koyeb.app
CORS_ORIGINS = *
```

**Port:**
- Port: `8000` (auto-detected)

**Health Check:**
- Path: `/api/`
- Port: `8000`
- Initial delay: `30` seconds

### 2.4 Deploy
Click **Deploy** button

---

## 🤖 Step 3: Bot Worker Service (Alag se)

Bot ke liye **separate service** banani hogi:

### 3.1 Create Bot Service

1. **Create New App**
2. Same repository select karo
3. **Service Name**: `ludo-bot-worker`

### 3.2 Configure Bot

**Build:**
- Builder: **Buildpack**
- Build command: Leave empty
- Run command: `python -m backend.bot_runner`

**Instance:**
- Type: **Nano** (Free)
- Regions: Same as backend

**Environment Variables** (Same as backend):
```
MONGO_URL = mongodb+srv://...
DB_NAME = ludo_club_db
TELEGRAM_BOT_TOKEN = 1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
WEB_APP_URL = https://your-frontend-url.koyeb.app
```

**Advanced Settings:**
- Health Checks: **DISABLE** (Turn OFF)
- Scaling: Min=1, Max=1

### 3.3 Deploy Bot
Click **Deploy**

---

## 🎨 Step 4: Frontend Service (Optional)

Agar frontend bhi Koyeb pe host karni hai:

### 4.1 Create Frontend Service

1. **Create New App**
2. Same repo
3. **Service Name**: `ludo-frontend`

### 4.2 Configure Frontend

**Build:**
- Builder: **Buildpack**
- Build command: 
  ```bash
  cd frontend && npm install && npm run build
  ```
- Run command: 
  ```bash
  npx serve -s frontend/build -l $PORT
  ```

**Environment Variables:**
```
REACT_APP_BACKEND_URL = https://ludo-backend-xxxxx.koyeb.app
```

**Port:** Auto (3000)

### 4.3 Deploy
Click **Deploy**

---

## 🔍 Step 5: Check Logs

Deployment ke baad:

1. **Backend Service** → **Logs** tab
2. Dekho koi error toh nahi

Expected logs:
```
✅ INFO:     Started server process
✅ INFO:     Waiting for application startup
✅ INFO:     Application startup complete
✅ INFO:     Uvicorn running on http://0.0.0.0:8000
```

---

## 🧪 Step 6: Test Karo

### Test Backend API
```bash
curl https://ludo-backend-xxxxx.koyeb.app/api/
```

Expected response:
```json
{"message": "Hello World"}
```

### Test Telegram Bot
1. Telegram me bot ko group me add karo
2. `/start` command bhejo
3. "Place New Table" button aana chahiye
4. Click karo → Web app open hona chahiye

---

## ❌ Agar Phir Bhi Error Aaye

### Option A: Use Docker Instead

Docker 100% kaam karega. Koyeb me:

1. **Builder**: Change to **Docker**
2. **Dockerfile path**: `/Dockerfile`
3. Build command: Leave empty
4. Environment variables: Same

### Option B: Detailed Logs Check

1. Build logs me exact error dekho
2. Scroll down to see full error message
3. Common errors:
   - Missing `requirements.txt` → Fixed ✅
   - Wrong Python version → Fixed (3.11) ✅
   - Import errors → Should be fixed now ✅

### Option C: Local Test Pehle

```bash
# Test locally first
cd /app
python main.py

# Should see:
# INFO: Uvicorn running on http://0.0.0.0:8000
```

---

## 📊 Final Service Setup

Aapko **teen services** chaiye hongi:

| Service | Type | Run Command | Port | Health Check |
|---------|------|-------------|------|--------------|
| `ludo-backend` | Web | `python main.py` | 8000 | `/api/` ✅ |
| `ludo-bot-worker` | Worker | `python -m backend.bot_runner` | - | ❌ OFF |
| `ludo-frontend` | Web | `npx serve -s frontend/build -l $PORT` | 3000 | `/` ✅ |

---

## 🎯 Environment Variables Summary

**ALL SERVICES need these:**

```bash
# MongoDB (from Atlas)
MONGO_URL=mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority

# Database name
DB_NAME=ludo_club_db

# Telegram bot token (from @BotFather)
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz

# Frontend URL (update after frontend deploys)
WEB_APP_URL=https://ludo-frontend-xxxxx.koyeb.app

# CORS (optional)
CORS_ORIGINS=*
```

**Frontend ONLY needs:**
```bash
REACT_APP_BACKEND_URL=https://ludo-backend-xxxxx.koyeb.app
```

---

## ✅ Success Checklist

- [ ] Files pushed to GitHub
- [ ] Old service deleted
- [ ] Backend service created with correct run command
- [ ] Environment variables set
- [ ] Service deployed successfully
- [ ] Backend API responds: `curl https://backend-url/api/`
- [ ] Bot worker service created (if needed)
- [ ] Bot responding in Telegram
- [ ] Frontend deployed (if using Koyeb)
- [ ] Web app opens in Telegram

---

**Ab aap Step 1 se shuru karo! GitHub pe push karo aur phir Koyeb me fresh service banao! 🚀**
