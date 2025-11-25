# 🔧 Koyeb Environment Variables Setup

## ❌ Error: KeyError: 'DB_NAME'

Ye error tab aata hai jab environment variables set nahi hain.

## ✅ SOLUTION: Environment Variables Set Karo

### Step 1: Koyeb Dashboard me Jao

1. Apni service open karo
2. **Settings** tab click karo
3. Neeche scroll karke **Environment** section dhundo

### Step 2: Required Variables Add Karo

Click on **"Add Variable"** aur ye sab ek ek karke add karo:

#### 1. MongoDB Connection

**Key:** `MONGO_URL`  
**Value:** 
```
mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
```

**Kahan se milega?**
- MongoDB Atlas dashboard
- Clusters → Connect → Connect your application
- Copy connection string
- Replace `<password>` with actual password

---

#### 2. Database Name

**Key:** `DB_NAME`  
**Value:** 
```
ludo_club_db
```

---

#### 3. Telegram Bot Token

**Key:** `TELEGRAM_BOT_TOKEN`  
**Value:** 
```
1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
```

**Kahan se milega?**
- Telegram me @BotFather open karo
- /mybots → Select your bot → API Token

---

#### 4. Web App URL

**Key:** `WEB_APP_URL`  
**Value:** 
```
https://ludo-frontend-xxxxx.koyeb.app
```

**Note:** Agar frontend abhi deploy nahi kiya toh:
- Pehle placeholder dalo: `https://example.com`
- Baad me update kar lena jab frontend deploy ho jaye

---

#### 5. CORS Origins (Optional)

**Key:** `CORS_ORIGINS`  
**Value:** 
```
*
```

---

#### 6. Port (Optional - Koyeb automatically sets)

**Key:** `PORT`  
**Value:** 
```
$PORT
```

**Note:** Usually ye automatically set hota hai, manually add karne ki zarurat nahi

---

### Step 3: Variables Verify Karo

Environment Variables section me ye sab dikhne chahiye:

```
MONGO_URL = mongodb+srv://...
DB_NAME = ludo_club_db
TELEGRAM_BOT_TOKEN = 123456...
WEB_APP_URL = https://...
CORS_ORIGINS = *
```

### Step 4: Service Redeploy Karo

1. **Save** button click karo (agar hai)
2. **Redeploy** button click karo
3. Ya simply **Settings** save karte hi auto-redeploy hoga

---

## 📸 Screenshot Reference

Environment variables section aisa dikhega:

```
┌─────────────────────────────────────────┐
│ Environment Variables                    │
├─────────────────────────────────────────┤
│ MONGO_URL          mongodb+srv://...    │
│ DB_NAME            ludo_club_db         │
│ TELEGRAM_BOT_TOKEN 123456:ABCdef...     │
│ WEB_APP_URL        https://frontend...  │
│ CORS_ORIGINS       *                    │
└─────────────────────────────────────────┘
```

---

## 🧪 Environment Test (Local)

Deployment se pehle local test kar sakte ho:

```bash
# Set environment variables
export MONGO_URL="your_mongo_url"
export DB_NAME="ludo_club_db"
export TELEGRAM_BOT_TOKEN="your_token"
export WEB_APP_URL="https://example.com"
export PORT="8000"

# Test
python test_env.py

# Run app
python main.py
```

---

## ✅ Complete Environment Variables List

### Backend Service

```bash
MONGO_URL=mongodb+srv://user:pass@cluster.mongodb.net/
DB_NAME=ludo_club_db
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
WEB_APP_URL=https://frontend-url.koyeb.app
CORS_ORIGINS=*
```

### Bot Worker Service (Same as backend)

```bash
MONGO_URL=mongodb+srv://user:pass@cluster.mongodb.net/
DB_NAME=ludo_club_db
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
WEB_APP_URL=https://frontend-url.koyeb.app
```

### Frontend Service

```bash
REACT_APP_BACKEND_URL=https://backend-url.koyeb.app
```

---

## 🔍 Verification Steps

After setting variables:

### 1. Check Logs

Service → Logs tab me ye dikhna chahiye:

```
✅ Starting Deep Night Ludo Club on port 8000
✅ Environment:
   - DB_NAME: ludo_club_db
   - MONGO_URL: mongodb+srv://...
   - PORT: 8000
✅ INFO: Started server process
✅ INFO: Uvicorn running on http://0.0.0.0:8000
```

### 2. Test API

```bash
curl https://your-backend-url.koyeb.app/api/
```

Should return:
```json
{"message": "Hello World"}
```

---

## ❌ Common Mistakes

1. **Password me special characters**
   - `@`, `#`, etc. ko URL encode karo
   - Example: `p@ss` → `p%40ss`

2. **Extra spaces**
   - Value me pehle ya baad me space nahi hona chahiye
   - ❌ ` mongodb://...`
   - ✅ `mongodb://...`

3. **Wrong connection string**
   - MongoDB Atlas ka full string use karo with `/`
   - ❌ `mongodb+srv://cluster.mongodb.net`
   - ✅ `mongodb+srv://user:pass@cluster.mongodb.net/`

4. **Missing question mark in MongoDB URL**
   - ❌ `...mongodb.net/retryWrites=true`
   - ✅ `...mongodb.net/?retryWrites=true`

---

## 🚨 If Still Error Persists

### Check MongoDB Atlas Settings:

1. **Network Access:**
   - IP Whitelist me `0.0.0.0/0` add karo
   - Security → Network Access → Add IP Address

2. **Database User:**
   - User exist karta hai?
   - Password correct hai?
   - Permissions: "Read and write to any database"

3. **Test Connection:**
   ```bash
   # Use mongosh to test
   mongosh "your_connection_string"
   ```

---

## 📞 Need MongoDB Atlas?

### Quick Setup:

1. **Sign up:** https://mongodb.com/cloud/atlas/register
2. **Create Free Cluster:**
   - Tier: M0 (Free)
   - Region: Closest to your users
   - Cluster Name: ludo-cluster

3. **Create User:**
   - Security → Database Access
   - Add New User
   - Username: `ludo_admin`
   - Password: Generate strong password
   - Built-in Role: Atlas admin

4. **Whitelist IP:**
   - Security → Network Access
   - Add IP Address: `0.0.0.0/0`

5. **Get Connection String:**
   - Clusters → Connect
   - Connect your application
   - Copy string

---

## ✅ After All Variables Set

Environment should look like this in Koyeb:

| Key | Value | Status |
|-----|-------|--------|
| MONGO_URL | mongodb+srv://... | ✅ Set |
| DB_NAME | ludo_club_db | ✅ Set |
| TELEGRAM_BOT_TOKEN | 123456... | ✅ Set |
| WEB_APP_URL | https://... | ✅ Set |
| CORS_ORIGINS | * | ✅ Set |

**Now Redeploy and check logs!** 🚀
