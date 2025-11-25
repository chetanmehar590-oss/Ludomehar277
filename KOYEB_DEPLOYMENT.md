# 🚀 Koyeb Deployment Guide - Deep Night Ludo Club Bot

## 📋 Prerequisites

1. **Koyeb Account** - https://app.koyeb.com (Free tier available)
2. **GitHub Repository** - Code push kar liya ho
3. **MongoDB Atlas Account** - Free tier: https://mongodb.com/atlas
4. **Telegram Bot Token** - @BotFather se

---

## 🗄️ Step 1: MongoDB Atlas Setup (Database)

Koyeb database provide nahi karta, isliye MongoDB Atlas use karenge:

### 1.1 Create MongoDB Atlas Cluster

1. https://mongodb.com/atlas par jayen
2. **Sign Up** karein (free)
3. **Create New Cluster** (Free M0 tier select karein)
4. Cluster name: `ludo-club-db`
5. Region: Choose closest to your users
6. Click **Create Cluster**

### 1.2 Create Database User

1. **Database Access** tab pe jayen
2. **Add New Database User**
3. Username: `ludo_admin`
4. Password: Generate strong password (save it!)
5. **Built-in Role**: Read and write to any database
6. **Add User**

### 1.3 Whitelist IP Address

1. **Network Access** tab pe jayen
2. **Add IP Address**
3. **Allow Access from Anywhere**: `0.0.0.0/0` (for Koyeb)
4. **Confirm**

### 1.4 Get Connection String

1. **Clusters** tab pe jayen
2. **Connect** button click karein
3. **Connect your application**
4. Copy connection string:
   ```
   mongodb+srv://ludo_admin:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
   ```
5. Replace `<password>` with actual password

---

## 🔧 Step 2: Prepare Code for Koyeb

### 2.1 Create Procfile for Backend

Koyeb ko batane ke liye ki kaise run karna hai:

```bash
# Create file: /app/Procfile
web: cd backend && uvicorn server:app --host 0.0.0.0 --port $PORT
worker: cd backend && python bot_runner.py
```

### 2.2 Create requirements.txt Root Level

```bash
# Copy backend requirements to root
cp /app/backend/requirements.txt /app/requirements.txt
```

### 2.3 Create runtime.txt (Optional)

```bash
# Tell Koyeb which Python version to use
echo "python-3.11.0" > /app/runtime.txt
```

---

## 🚀 Step 3: Deploy Backend on Koyeb

### 3.1 Create Backend Service

1. **Koyeb Dashboard** me jayen
2. **Create App** click karein
3. **GitHub** select karein
4. Repository select karein
5. **Service Name**: `ludo-club-backend`

### 3.2 Configure Build Settings

**Builder**: Buildpack

**Build Command**:
```bash
pip install -r requirements.txt
```

**Run Command**:
```bash
cd backend && uvicorn server:app --host 0.0.0.0 --port $PORT
```

### 3.3 Environment Variables (IMPORTANT!)

Koyeb me **Environment Variables** section me ye sab add karein:

```bash
# MongoDB
MONGO_URL=mongodb+srv://ludo_admin:YOUR_PASSWORD@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
DB_NAME=ludo_club_db

# Telegram Bot
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz

# Web App URL (frontend URL - Step 4 ke baad update karenge)
WEB_APP_URL=https://your-frontend-url.koyeb.app

# CORS
CORS_ORIGINS=*

# Port (Koyeb automatically provides this)
PORT=8000
```

### 3.4 Deploy

1. **Instance Type**: Free (Nano)
2. **Region**: Choose nearest
3. Click **Deploy**
4. Wait 2-3 minutes for deployment

### 3.5 Get Backend URL

Deployment complete hone ke baad:
- URL milega: `https://ludo-club-backend-xxxxx.koyeb.app`
- Save this URL!

---

## 🎨 Step 4: Deploy Frontend on Koyeb

### 4.1 Update Frontend .env

Pehle local me update karein:

```bash
# /app/frontend/.env
REACT_APP_BACKEND_URL=https://ludo-club-backend-xxxxx.koyeb.app
```

Commit and push to GitHub:

```bash
git add frontend/.env
git commit -m "Update backend URL for Koyeb"
git push origin main
```

### 4.2 Create Frontend Service

1. **Create New App** in Koyeb
2. Select same GitHub repo
3. **Service Name**: `ludo-club-frontend`

### 4.3 Configure Build Settings

**Builder**: Buildpack

**Build Command**:
```bash
cd frontend && yarn install && yarn build
```

**Run Command**:
```bash
cd frontend && npx serve -s build -l $PORT
```

### 4.4 Environment Variables

```bash
REACT_APP_BACKEND_URL=https://ludo-club-backend-xxxxx.koyeb.app
PORT=3000
```

### 4.5 Deploy

1. **Instance Type**: Free (Nano)
2. **Region**: Same as backend
3. Click **Deploy**

### 4.6 Get Frontend URL

- Frontend URL: `https://ludo-club-frontend-xxxxx.koyeb.app`
- Save this URL!

---

## 🤖 Step 5: Deploy Telegram Bot Worker

### 5.1 Create Bot Worker Service

1. **Create New App** in Koyeb
2. Select same GitHub repo
3. **Service Name**: `ludo-club-bot`

### 5.2 Configure Build Settings

**Builder**: Buildpack

**Build Command**:
```bash
pip install -r requirements.txt
```

**Run Command**:
```bash
cd backend && python bot_runner.py
```

### 5.3 Environment Variables

```bash
# Same as backend
MONGO_URL=mongodb+srv://ludo_admin:YOUR_PASSWORD@cluster0.xxxxx.mongodb.net/
DB_NAME=ludo_club_db
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
WEB_APP_URL=https://ludo-club-frontend-xxxxx.koyeb.app
```

### 5.4 Advanced Settings

- **Instance Type**: Free (Nano)
- **Health Checks**: Disable (bot doesn't expose HTTP endpoint)
- **Scaling**: Min=1, Max=1 (keep one instance running)

### 5.5 Deploy

Click **Deploy** and wait!

---

## 🔄 Step 6: Update Backend with Frontend URL

Backend service me jakar **WEB_APP_URL** update karein:

1. Backend service open karein
2. **Settings** → **Environment Variables**
3. `WEB_APP_URL` ko update karein:
   ```
   WEB_APP_URL=https://ludo-club-frontend-xxxxx.koyeb.app
   ```
4. **Redeploy** karein

---

## ✅ Step 7: Configure Telegram Bot

### 7.1 Set Bot Domain

Telegram me @BotFather ko message karein:

```
/mybots
[Select your bot]
/setdomain
[Enter: https://ludo-club-frontend-xxxxx.koyeb.app]
```

### 7.2 Set Bot Commands

```
/mybots
[Select your bot]
/setcommands

start - Get started and show table button
help - Show help message
table - Send 'Place New Table' button
```

---

## 🧪 Step 8: Testing

### Test Backend API

```bash
curl https://ludo-club-backend-xxxxx.koyeb.app/api/
# Should return: {"message":"Hello World"}
```

### Test Frontend

Open browser: `https://ludo-club-frontend-xxxxx.koyeb.app`

### Test Telegram Bot

1. Add bot to a Telegram group
2. Send `/start` command
3. Click "Place New Table" button
4. Web app should open inside Telegram
5. Fill form and submit
6. Check if data appears in Last Table Request

---

## 📊 Step 9: Monitor Services

### Koyeb Dashboard

1. **Services** tab me jayen
2. Teen services hongi:
   - ✅ `ludo-club-backend` (Running)
   - ✅ `ludo-club-frontend` (Running)
   - ✅ `ludo-club-bot` (Running)

### View Logs

Each service me:
1. Service name click karein
2. **Logs** tab pe jayen
3. Real-time logs dekhein

### Check Health

```bash
# Backend health
curl https://ludo-club-backend-xxxxx.koyeb.app/api/

# Check tables API
curl https://ludo-club-backend-xxxxx.koyeb.app/api/tables
```

---

## 🎯 Final Configuration Summary

### Environment Variables Needed:

**Backend Service:**
```bash
MONGO_URL=mongodb+srv://user:pass@cluster.mongodb.net/
DB_NAME=ludo_club_db
TELEGRAM_BOT_TOKEN=your_bot_token
WEB_APP_URL=https://your-frontend.koyeb.app
CORS_ORIGINS=*
```

**Frontend Service:**
```bash
REACT_APP_BACKEND_URL=https://your-backend.koyeb.app
```

**Bot Worker Service:**
```bash
MONGO_URL=mongodb+srv://user:pass@cluster.mongodb.net/
DB_NAME=ludo_club_db
TELEGRAM_BOT_TOKEN=your_bot_token
WEB_APP_URL=https://your-frontend.koyeb.app
```

---

## 🐛 Troubleshooting

### Backend Not Starting?

**Check Logs:**
- Koyeb Dashboard → Backend Service → Logs
- Look for errors

**Common Issues:**
- ❌ Wrong MongoDB connection string
- ❌ Missing environment variables
- ❌ Wrong PORT configuration

**Fix:**
```bash
# Make sure these are set:
MONGO_URL=mongodb+srv://...
PORT=$PORT  # Koyeb provides this automatically
```

### Frontend Not Loading?

**Check:**
- ✅ `REACT_APP_BACKEND_URL` is correct
- ✅ Backend is running
- ✅ CORS is enabled on backend

### Bot Not Responding?

**Check:**
1. Bot worker service is running
2. `TELEGRAM_BOT_TOKEN` is correct
3. Check bot worker logs in Koyeb
4. Verify bot is not blocked in group

### Database Connection Failed?

**Check:**
1. MongoDB Atlas cluster is running
2. IP whitelist includes `0.0.0.0/0`
3. Database user has correct permissions
4. Connection string password is correct

---

## 💰 Koyeb Free Tier Limits

- **3 Free Services** (perfect for our 3 services!)
- **512 MB RAM per service**
- **1 vCPU per service**
- **No credit card required**
- **2.5M requests/month**

---

## 🔄 Redeployment

Koyeb automatically redeploys when you push to GitHub:

```bash
# Make changes
git add .
git commit -m "Update features"
git push origin main

# Koyeb will auto-deploy in ~2-3 minutes
```

---

## 🎉 You're Live!

Aapka Deep Night Ludo Club Bot ab live hai:

✅ **Backend**: API running on Koyeb
✅ **Frontend**: Web app on Koyeb
✅ **Bot**: Telegram bot worker running
✅ **Database**: MongoDB Atlas
✅ **HTTPS**: Automatic SSL

**Share Your Bot:**
```
https://t.me/YourBotUsername
```

---

## 📞 Need Help?

- **Koyeb Docs**: https://www.koyeb.com/docs
- **MongoDB Atlas Docs**: https://docs.atlas.mongodb.com/
- **Telegram Bot API**: https://core.telegram.org/bots/api

**Happy Gaming! 🎲🎮**
