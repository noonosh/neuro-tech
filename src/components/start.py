from telegram import Update
from telegram.ext import CallbackContext
from utils.text import text
from . import index


def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    update.effective_message.reply_text(
        text('greet'), parse_mode='HTML')
    return index.display(update, context)
