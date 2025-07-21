from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "7192654707:AAGEzQdebS0qjMxALCq44K6N0A2NEOgyVB0"  # Ton token

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("🎉 BIENVENUE DANS TON PREMIER BOT TELEGRAM 🎉")

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
