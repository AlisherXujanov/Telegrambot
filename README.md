
# Introduction
1. From telegram BotFather you will get a token that you need to get started with the bot. 
2. Create a python file and write your token in it. 
3. Install the python-telegram-bot library using pip install python-telegram-bot  
```bash
pip install python-telegram-bot
```
4. Create a bot instance using the token you got from the BotFather.
5. Create a function that will be called whenever a user sends a message to the bot.
   ex:  
```python
def start(update, context):
    context.bot.send_message("Hello World")
```


---
# Buttons
<!-- BUTTONS -->
The python-telegram-bot library supports two types of buttons: InlineKeyboardButton and KeyboardButton.

- InlineKeyboardButton: These buttons are often used within a custom keyboard for inline queries. When the user clicks an inline button, Telegram clients will display a progress bar until you call answerCallbackQuery. Here's an example of how to use it:
```python
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler

def start(update, context):
    keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
                 InlineKeyboardButton("Option 2", callback_data='2')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
```

- KeyboardButton: These buttons are part of a custom keyboard attached to the message. They are simpler than inline buttons. Here's an example of how to use it:
```python
from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CommandHandler

def start(update, context):
    keyboard = [[KeyboardButton("Option 1"), KeyboardButton("Option 2")]]

    reply_markup = ReplyKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
```

In both examples, when the /start command is sent, a message with a custom keyboard is sent. The user can then select an option from the keyboard.


# To create requirements.txt file
1. ```pipenv lock -r > requirements.txt```  - is outdated
2. 🎯 New version is: ```pipenv run pip freeze  > requirements.txt``` 