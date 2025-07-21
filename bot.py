from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import timezone

TOKEN = "7192654707:AAGEzQdebS0qjMxALCq44K6N0A2NEOgyVB0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎉 Bienvenue dans ton bot Telegram !")

def main():
    application = ApplicationBuilder().token(TOKEN).build()

    # Configuration du scheduler (SANS créer un JobQueue manuellement)
    scheduler = AsyncIOScheduler(timezone=timezone("Africa/Ouagadougou"))
    application.job_queue.scheduler = scheduler

    application.add_handler(CommandHandler("start", start))

    application.run_polling()

if __name__ == "__main__":
    main()
