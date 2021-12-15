from telegram.ext import CallbackContext
from telegram import Update
from utils.text import text


def help(update: Update, context: CallbackContext):
    """
    Send a friendly message to help to navigate the user in the bot
    """
    update.effective_message.reply_text(text('help'), parse_mode="HTML")


def cancel(update: Update, context: CallbackContext):
    """
    Cancel the current operation. Return to main section if successful
    """
    pass


def code(update: Update, context: CallbackContext):
    """
    Randomly choose a code snippet from the backend service. **NEEDS TO BE IMPLEMENTED**
    """
    pass


def explore(update: Update, context: CallbackContext):
    """
    Navigate to explore section
    """
    pass
