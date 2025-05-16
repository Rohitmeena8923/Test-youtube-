import os
import logging
from telegram.ext import Application
from bot.handlers import register_handlers
from bot.utils.logger import configure_logging
from config.settings import TELEGRAM_TOKEN, WEBHOOK_URL, PORT, WEBHOOK_SECRET

def create_app():
    """Initialize the Telegram bot application"""
    configure_logging()
    os.makedirs("data/downloads", exist_ok=True)
    
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    register_handlers(application)
    return application

def main():
    app = create_app()
    
    if WEBHOOK_URL:
        app.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            webhook_url=WEBHOOK_URL,
            secret_token=WEBHOOK_SECRET,
        )
    else:
        app.run_polling()

if __name__ == "__main__":
    main()