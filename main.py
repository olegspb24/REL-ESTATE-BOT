from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests
from config import TELEGRAM_TOKEN, WEBHOOK_URL

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Здравствуйте! Укажите, пожалуйста, ваш бюджет.")

def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    user_id = update.effective_user.id
    requests.post(WEBHOOK_URL, json={
        "user_id": user_id,
        "message": user_message
    })
    update.message.reply_text("Спасибо! Мы получили вашу заявку.")

def main():
    updater = Updater(TELEGRAM_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
