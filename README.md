# 🎲 Deep Night Ludo Club Bot

A full-stack web application clone of the Deep Night Ludo Club Telegram bot with complete Telegram integration.

## 🌟 Features

### Web Application
- ✅ Table booking system with multiple game types
- ✅ Balance management
- ✅ Last table request tracking
- ✅ Quick amount selection buttons
- ✅ Game+ configuration
- ✅ Multiple game options (Fresh Id, Code aap doge, No iPhone, etc.)
- ✅ Form validation and error handling
- ✅ Toast notifications
- ✅ Responsive design

### Telegram Bot Integration
- ✅ Send "Place New Table" button in groups
- ✅ Telegram Mini App integration
- ✅ Opens web app inside Telegram
- ✅ Bot commands (/start, /help, /table)
- ✅ Works in groups and private chats

## 🎮 Game Types

1. Full
2. Ulta
3. Popular
4. 3 Goti
5. 2 Goti
6. 1 Goti
7. 1 Goti Quick
8. Snake
9. Ulta Snake
10. Snake Re-Roll
11. Not Cut

## 🛠️ Tech Stack

### Frontend
- React 19
- Tailwind CSS
- shadcn/ui components
- React Router
- Axios

### Backend
- FastAPI
- Python 3.11
- MongoDB (Motor)
- python-telegram-bot

## 📦 Installation

### Prerequisites
- Node.js 18+
- Python 3.11+
- MongoDB
- Telegram Bot Token (from @BotFather)

### Setup

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd <repo-name>
```

2. **Backend Setup**
```bash
cd backend
pip install -r requirements.txt

# Copy and configure environment variables
cp .env.example .env
# Edit .env and add your configuration
```

3. **Frontend Setup**
```bash
cd frontend
yarn install
```

4. **Configure Environment Variables**

Edit `/app/backend/.env`:
```bash
MONGO_URL=mongodb://localhost:27017/
DB_NAME=ludo_club_db
TELEGRAM_BOT_TOKEN=your_bot_token_here
WEB_APP_URL=https://your-app-url.com
```

## 🚀 Running the Application

### Development Mode

**Frontend:**
```bash
cd frontend
yarn start
```

**Backend:**
```bash
cd backend
uvicorn server:app --reload --host 0.0.0.0 --port 8001
```

**Telegram Bot:**
```bash
cd backend
python bot_runner.py
```

### Production Mode

```bash
sudo supervisorctl restart all
```

## 🤖 Telegram Bot Setup

Detailed Telegram bot setup instructions are available in [TELEGRAM_BOT_SETUP.md](./TELEGRAM_BOT_SETUP.md)

### Quick Start:

1. Get bot token from [@BotFather](https://t.me/botfather)
2. Add token to `.env` file
3. Deploy your web app (HTTPS required)
4. Update `WEB_APP_URL` in `.env`
5. Run the bot: `python backend/bot_runner.py`
6. Add bot to your Telegram group
7. Use `/start` command in group

## 📱 Usage

### Web Interface
1. Open the web app
2. Fill in the table details:
   - Amount (or use quick selection)
   - Game Type
   - Game+ value
   - Select options
3. Agree to game rules
4. Click "Send Table"

### Telegram Bot
1. Add bot to your group
2. Type `/start` or `/table`
3. Click "🎲 Place New Table" button
4. Web app opens inside Telegram
5. Fill and submit the form

## 🎯 API Endpoints

### Backend API
- `GET /api/` - Health check
- `POST /api/tables` - Create new table request
- `GET /api/tables` - Get all table requests
- `GET /api/tables/{id}` - Get specific table
- `PUT /api/tables/{id}` - Update table
- `DELETE /api/tables/{id}` - Delete table
- `GET /api/user/balance` - Get user balance

## 📁 Project Structure

```
/app
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   └── ui/          # shadcn components
│   │   ├── pages/
│   │   │   └── HomePage.jsx # Main page
│   │   ├── hooks/
│   │   ├── mock.js          # Mock data
│   │   ├── App.js
│   │   └── index.css
│   └── package.json
├── backend/
│   ├── server.py            # FastAPI server
│   ├── telegram_bot.py      # Telegram bot
│   ├── bot_runner.py        # Bot starter
│   ├── requirements.txt
│   └── .env
├── TELEGRAM_BOT_SETUP.md    # Bot setup guide
└── README.md
```

## 🔒 Security Notes

- ⚠️ Never commit `.env` file to GitHub
- ⚠️ Keep your bot token secret
- ⚠️ Use HTTPS for production
- ⚠️ Validate all user inputs
- ⚠️ Set proper CORS configuration

## 🐛 Troubleshooting

### Bot not responding?
- Check if `TELEGRAM_BOT_TOKEN` is correct
- Verify bot is running: `ps aux | grep bot_runner`
- Check logs for errors

### Web app not opening in Telegram?
- Ensure `WEB_APP_URL` is HTTPS
- Configure domain in @BotFather
- Check if app is accessible

### Database connection issues?
- Verify MongoDB is running
- Check `MONGO_URL` in `.env`
- Ensure database exists

## 📝 License

MIT License

## 👨‍💻 Author

Created with ❤️ for Deep Night Ludo Club

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

**Happy Gaming! 🎲🎮**
