import logging
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters
)
KEY = "6843019542:AAGPegaQeik5rpZSYY_vi4lmV4KvmbqiPpU"


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes) -> None:
    return await update.message.reply_text("Hello world!")


async def help(update: Update, context: ContextTypes) -> None:
    return await update.message.reply_text("""
/help - Show this message
/start - Start the bot
""")


# Response
async def handle_responses(update:Update, context:ContextTypes) -> str:
    text: str = update.message.text.lower()

    response = ""

    if 'hello' in text:
        response = "Hello there! How can i help you? \n" #  \n  ->  is a new line
    if "how are you" in text:
        response = response + "I'm fine, thank you. And you? \n"

    return await update.message.reply_text(response)


# Run the bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(KEY).build()
    print("Bot is running...")

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_responses))


    # Run the bot
    print("Polling...")
    app.run_polling(poll_interval=1)
