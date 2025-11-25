# 🚀 Quick Start Guide - Deep Night Ludo Club Bot

## 📦 Koyeb Deployment - 5 Minutes Setup

### 1️⃣ MongoDB Atlas (2 min)
```
1. https://mongodb.com/atlas → Sign Up (Free)
2. Create Cluster (M0 Free tier)
3. Database Access → Add User
4. Network Access → Allow 0.0.0.0/0
5. Copy Connection String:
   mongodb+srv://username:password@cluster.mongodb.net/
```

### 2️⃣ Telegram Bot (1 min)
```
1. Telegram me @BotFather open karein
2. /newbot → Bot Name → Bot Username
3. Copy Bot Token: 1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
```

### 3️⃣ GitHub Push (1 min)
```bash
git add .
git commit -m "Ready for Koyeb deployment"
git push origin main
```

### 4️⃣ Koyeb Deploy (2 min)

**Service 1: Backend**
- Name: `ludo-club-backend`
- Run: `cd backend && uvicorn server:app --host 0.0.0.0 --port $PORT`
- Env Vars:
  ```
  MONGO_URL=mongodb+srv://...
  DB_NAME=ludo_club_db
  TELEGRAM_BOT_TOKEN=your_token
  WEB_APP_URL=https://frontend-url (update later)
  ```

**Service 2: Frontend**
- Name: `ludo-club-frontend`
- Build: `cd frontend && yarn install && yarn build`
- Run: `cd frontend && npx serve -s build -l $PORT`
- Env Vars:
  ```
  REACT_APP_BACKEND_URL=https://backend-url
  ```

**Service 3: Bot Worker**
- Name: `ludo-club-bot`
- Run: `cd backend && python bot_runner.py`
- Same env vars as Backend

### 5️⃣ Configure Bot
```
@BotFather me:
/setdomain → https://your-frontend-url.koyeb.app
/setcommands → paste commands
```

---

## ✅ Required Environment Variables

### Backend & Bot Worker
| Variable | Example | Where to Get |
|----------|---------|--------------|
| `MONGO_URL` | `mongodb+srv://user:pass@...` | MongoDB Atlas |
| `DB_NAME` | `ludo_club_db` | Your choice |
| `TELEGRAM_BOT_TOKEN` | `123:ABCdef...` | @BotFather |
| `WEB_APP_URL` | `https://frontend.koyeb.app` | Koyeb frontend URL |

### Frontend
| Variable | Example | Where to Get |
|----------|---------|--------------|
| `REACT_APP_BACKEND_URL` | `https://backend.koyeb.app` | Koyeb backend URL |

---

## 🧪 Testing Checklist

- [ ] Backend API working: `curl https://backend-url/api/`
- [ ] Frontend loading: Open in browser
- [ ] Bot responding: `/start` in Telegram
- [ ] Button appears in group
- [ ] Web app opens inside Telegram
- [ ] Form submission works
- [ ] Data saves to database

---

## 📞 Important URLs

After deployment, save these:

```
Backend:  https://ludo-club-backend-xxxxx.koyeb.app
Frontend: https://ludo-club-frontend-xxxxx.koyeb.app
Bot:      https://t.me/YourBotUsername
Database: MongoDB Atlas Dashboard
```

---

## 🎯 Common Issues & Fixes

| Issue | Solution |
|-------|----------|
| Bot not responding | Check bot worker logs in Koyeb |
| Web app not opening | Verify domain set in @BotFather |
| Database error | Check MongoDB connection string |
| CORS error | Add `CORS_ORIGINS=*` to backend |

---

## 💡 Pro Tips

1. **Free Tier**: Koyeb gives 3 free services (perfect!)
2. **Auto Deploy**: Push to GitHub → Auto deploys
3. **Logs**: Check Koyeb dashboard for errors
4. **Environment**: Never commit `.env` to GitHub
5. **MongoDB**: Use Atlas free tier (512 MB)

---

## 📚 Full Guides

- **Detailed Deployment**: See `KOYEB_DEPLOYMENT.md`
- **Telegram Bot Setup**: See `TELEGRAM_BOT_SETUP.md`
- **General Deployment**: See `DEPLOYMENT_GUIDE.md`

---

**🎉 Your bot will be live in 5 minutes!**
