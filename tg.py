# pipenv install python-telegram-bot

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
    filters,
    CallbackQueryHandler
)
KEY = "6843019542:AAGPegaQeik5rpZSYY_vi4lmV4KvmbqiPpU"


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


# async def block_button(update: Update, context: ContextTypes) -> None:
#     """Sends a message with three inline buttons attached."""
#     keyboard = [
#         [KeyboardButton("Option 1"), KeyboardButton("Option 2")],
#         [KeyboardButton("Option 3")],
#     ]
#     reply_markup = ReplyKeyboardMarkup(keyboard)
#     await update.message.reply_text("Please choose:", reply_markup=reply_markup)


async def start(update: Update, context: ContextTypes) -> None:
    """Sends a message with three inline buttons attached."""
    # keyboard = [
    #     [
    #         InlineKeyboardButton("Option 1", callback_data="1"),
    #         InlineKeyboardButton("Option 2", callback_data="2"),
    #     ],
    #     [InlineKeyboardButton("Option 3", callback_data="3")],
    # ]
    # reply_markup = InlineKeyboardMarkup(keyboard)
    # await update.message.reply_text("Please choose:", reply_markup=reply_markup)
    await update.message.reply_text("Hello world! This is me!")


async def inline_button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"Selected option: {query.data}")

    if query.data == "1":
        await query.edit_message_text(text="You pressed button 1")

    elif query.data == "2":
        await query.edit_message_text(text="You pressed button 2")
    elif query.data == "3":
        await query.edit_message_text(text="You pressed button 3")
    elif query.data == "4":
        await query.edit_message_text(text="You pressed button 4")

    # If we want to answer the button by using another button we can use this:
    return await query.edit_message_text(
        text=f"Selected option: {query.data}",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Answer", callback_data="4")]])
    )




async def help(update: Update, context: ContextTypes) -> None:
    return await update.message.reply_text("""
/help - Show this message
/start - Start the bot
""")


# Response
async def handle_responses(update: Update, context: ContextTypes) -> str:
    text:str = update.message.text.lower()

    username = update.message.from_user.username
    print(f"User {username} sent: {text}")

    response = ""

    if 'hello' in text:
        response = f"Hello there {username}! How can i help you? \n"  # \n  ->  is a new line
    if "how are you" in text:
        response = response + "I'm fine, thank you. And you? \n"

    with open("me.jpg", "rb") as f:
        """
                update.message.reply_photo(photo, caption=None)
            photo   - Photo to send
            caption - Photo caption, 0-1024 characters
        """
        await update.message.reply_photo(f, caption="Hello world! This is me!")
        
    await update.message.reply_text(response)


# Run the bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(KEY).build()
    print("Bot is running...")

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))

    # # Inline button
    # app.add_handler(CallbackQueryHandler(inline_button_handler))
    # # Block button
    # app.add_handler(CommandHandler("bbutton", block_button))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_responses))

    # Run the bot
    print("Polling...")
    app.run_polling(poll_interval=1)
