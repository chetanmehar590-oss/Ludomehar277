# 🔧 Koyeb Frontend Deployment Fix

## ❌ Error: Failed to build - exit status 127

**Problem:** Koyeb Python buildpack detect kar raha hai instead of Node.js

---

## ✅ Solution 1: Docker Use Karo (Best)

### Step 1: Delete Old Frontend Service

1. Koyeb → Services → **ludo-frontend**
2. Settings → Scroll down
3. **Delete Service**

### Step 2: Create New Service with Docker

1. **Create App**
2. GitHub repository select
3. **Service name:** `ludo-frontend`

### Step 3: Configuration

**Builder:** Select **Docker**

**Dockerfile path:**
```
Dockerfile.frontend
```

**Build command:** Leave EMPTY

**Run command:** Leave EMPTY (Docker handles it)

**Port:** `3000`

**Environment Variables:**
```
REACT_APP_BACKEND_URL = https://integral-marcile-chetan1-34ba91a5.koyeb.app
```

**Instance:** Nano (Free)

**Deploy!**

---

## ✅ Solution 2: Force Node.js Buildpack

Agar Docker use nahi karna chahte:

### Create `.buildpacks` File

Koyeb ko batane ke liye ki Node.js use karna hai:

Create `/app/.buildpacks`:
```
https://github.com/heroku/heroku-buildpack-nodejs
```

### Koyeb Configuration

**Builder:** Buildpack

**Build command:**
```bash
yarn install && cd frontend && yarn install && yarn build
```

**Run command:**
```bash
npx serve -s frontend/build -l $PORT
```

---

## ✅ Solution 3: Separate Frontend Repo (Alternative)

Agar ye solutions kaam nahi kare, frontend ko alag repo me deploy karo:

### Quick Steps:

1. New GitHub repo banao: `ludo-frontend`
2. Only `frontend/` folder ki files copy karo
3. Koyeb me us repo se deploy karo

---

## 📋 Expected Success Logs

Successful deployment me ye dikhna chahiye:

```
✅ Node.js detected
✅ Installing node modules
✅ Building React app
✅ Build complete
✅ Starting server
✅ Server listening on port 3000
```

**NOT:**
```
❌ Python 3.11 detected
❌ Installing python packages
```

---

## 🚀 After Successful Deploy

1. Frontend URL milega: `https://ludo-frontend-xxxxx.koyeb.app`
2. Browser me open karo - form dikhna chahiye
3. Bot me `WEB_APP_URL` update karo
4. BotFather me domain set karo
5. Test karo!

---

## 🐛 If Docker Also Fails

Check these:

1. **Dockerfile exists?**
   ```bash
   git ls-files | grep Dockerfile.frontend
   ```

2. **Frontend files exist?**
   ```bash
   git ls-files frontend/
   ```

3. **Files pushed to GitHub?**
   ```bash
   git push origin main
   ```

---

## 💡 Quick Test Locally

```bash
# Test Docker build
docker build -f Dockerfile.frontend -t ludo-frontend .

# Run
docker run -p 3000:3000 ludo-frontend

# Open: http://localhost:3000
```

---

**Recommendation:** Use Docker (Solution 1) for most reliable deployment! 🐳
