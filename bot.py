from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Это JetX Strategy Bot 🚀")

app = ApplicationBuilder().token("ВАШ_ТОКЕН_ТУТ").build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
