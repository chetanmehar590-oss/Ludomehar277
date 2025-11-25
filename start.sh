#!/bin/bash

# Start script for Koyeb deployment
# This script handles backend startup with proper PORT binding

# Get PORT from environment or use default
PORT=${PORT:-8000}

echo "🚀 Starting Deep Night Ludo Club Backend..."
echo "📡 Port: $PORT"
echo "🗄️  MongoDB: $MONGO_URL"
echo "🤖 Bot Token: ${TELEGRAM_BOT_TOKEN:0:10}..."

# Start the server
uvicorn backend.server:app --host 0.0.0.0 --port $PORT
