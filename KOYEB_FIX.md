# 🔧 Koyeb Deployment Fix - Error 255

## ❌ Common Error: "Application exited with code 255"

### 🎯 Solution 1: Correct Run Commands

#### Backend Service Configuration

**Build Command:**
```bash
pip install -r backend/requirements.txt
```

**Run Command:**
```bash
uvicorn backend.server:app --host 0.0.0.0 --port $PORT
```

**Important:** 
- Use `backend.server:app` NOT `cd backend && ...`
- Koyeb needs direct Python module path
- Port MUST be `$PORT` (Koyeb provides this)

---

#### Bot Worker Service Configuration

**Build Command:**
```bash
pip install -r backend/requirements.txt
```

**Run Command:**
```bash
python -m backend.bot_runner
```

**Important:**
- Use `python -m backend.bot_runner` NOT `cd backend && python bot_runner.py`
- Bot worker doesn't need PORT binding
- Disable health checks for bot worker

---

#### Frontend Service Configuration

**Build Command:**
```bash
cd frontend && npm install && npm run build
```

**Run Command:**
```bash
npx serve -s frontend/build -l $PORT
```

---

## 🔧 Fix Step-by-Step

### Fix 1: Update Backend Run Command

1. Go to **Backend Service** in Koyeb
2. Click **Settings**
3. Scroll to **Run command**
4. Change to:
   ```bash
   uvicorn backend.server:app --host 0.0.0.0 --port $PORT
   ```
5. Click **Save & Redeploy**

### Fix 2: Update Bot Worker

1. Go to **Bot Worker Service**
2. Click **Settings**
3. **Run command:**
   ```bash
   python -m backend.bot_runner
   ```
4. **Advanced Settings:**
   - Toggle OFF "Health checks"
   - Or set: Health check path = `/` (if HTTP port is exposed)
5. Click **Save & Redeploy**

### Fix 3: Check Environment Variables

Make sure these are set correctly:

**Backend & Bot Worker:**
```bash
MONGO_URL=mongodb+srv://username:password@cluster.mongodb.net/
DB_NAME=ludo_club_db
TELEGRAM_BOT_TOKEN=1234567890:ABCdef...
WEB_APP_URL=https://your-frontend-url.koyeb.app
PORT=$PORT
```

**Frontend:**
```bash
REACT_APP_BACKEND_URL=https://your-backend-url.koyeb.app
```

---

## 🛠️ Alternative: Single Service Approach

If multi-service is causing issues, deploy as single service:

### Procfile Method

Create `/app/Procfile`:
```
web: uvicorn backend.server:app --host 0.0.0.0 --port $PORT
```

Then in Koyeb:
- **Builder:** Dockerfile or Buildpack
- **Run command:** Leave empty (uses Procfile)

---

## 🐳 Docker Approach (Most Reliable)

### Create Dockerfile

```dockerfile
# /app/Dockerfile

FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/ ./backend/

# Expose port
EXPOSE 8000

# Run application
CMD ["uvicorn", "backend.server:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Koyeb Configuration

1. **Builder:** Docker
2. **Dockerfile path:** `/app/Dockerfile`
3. **Port:** 8000
4. Environment variables same as before

---

## 🔍 Debug Commands

### Test Locally First

```bash
# Test backend
cd /app
uvicorn backend.server:app --host 0.0.0.0 --port 8000

# Test bot
python -m backend.bot_runner

# Test if imports work
python -c "from backend.server import app; print('✅ Import successful')"
```

### Check Koyeb Logs

1. Service → **Logs** tab
2. Look for specific errors:
   - Module not found → Wrong path
   - Port binding error → Wrong PORT config
   - Import error → Missing dependencies

---

## ✅ Working Configuration Summary

### Backend Service

```yaml
Name: ludo-backend
Builder: Buildpack
Build: pip install -r backend/requirements.txt
Run: uvicorn backend.server:app --host 0.0.0.0 --port $PORT
Port: $PORT (auto)
Health Check: / or /api/
Instance: Nano (Free)
```

### Bot Worker Service

```yaml
Name: ludo-bot
Builder: Buildpack
Build: pip install -r backend/requirements.txt
Run: python -m backend.bot_runner
Health Check: DISABLED
Instance: Nano (Free)
```

### Frontend Service

```yaml
Name: ludo-frontend
Builder: Buildpack
Build: cd frontend && npm install && npm run build
Run: npx serve -s frontend/build -l $PORT
Port: $PORT (auto)
Instance: Nano (Free)
```

---

## 🚨 If Still Not Working

### Option A: Deploy Backend First

1. Only deploy backend service
2. Test if it works: `curl https://backend-url/api/`
3. Once working, deploy frontend
4. Then deploy bot worker

### Option B: Use Railway Instead

Railway has better error messages and is easier to debug:

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Deploy
railway up
```

### Option C: Check MongoDB Connection

```python
# Test MongoDB locally
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

async def test():
    client = AsyncIOMotorClient("your_mongo_url")
    db = client.test_db
    result = await db.test_collection.insert_one({"test": "data"})
    print(f"✅ MongoDB working: {result.inserted_id}")

asyncio.run(test())
```

---

## 📝 Checklist Before Redeploying

- [ ] Run command uses `backend.server:app` format
- [ ] Port is set to `$PORT`
- [ ] All environment variables are set
- [ ] MongoDB connection string is correct
- [ ] Bot token is valid
- [ ] requirements.txt is in backend folder
- [ ] Health checks configured correctly

---

## 💡 Pro Tip

Test your deployment config locally first:

```bash
# Simulate Koyeb environment
export PORT=8000
export MONGO_URL="your_mongo_url"
export TELEGRAM_BOT_TOKEN="your_token"

# Run as Koyeb would
uvicorn backend.server:app --host 0.0.0.0 --port $PORT
```

If this works locally, it should work on Koyeb!

---

**Need more help? Share the full error logs from Koyeb! 📊**
