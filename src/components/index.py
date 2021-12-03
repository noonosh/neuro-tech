from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext


def display(update: Update, context: CallbackContext):

    markup = [
        ['button 1'], ['button 2', 'button 3'], ['button 4']
    ]
    update.effective_message.reply_text('This is a main page',
                                        reply_markup=ReplyKeyboardMarkup(markup,
                                                                         resize_keyboard=True))
    return "INDEX PAGE"
