from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Define your bot token
BOT_TOKEN = '7889305935:AAEGiJHYi1o0cyibzpGebdhf_QgbL4RL9DY'

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to VivBot!\n\n"
        "Get real-time updates about Vivdisk and VDX Player launches.\n"
        "Type to see what I can do!"
    )

# Run the bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("🤖 VivBot is running...")
    app.run_polling()
