from logging import DEBUG
from telegram.ext import (Updater,
                          CommandHandler,
                          CallbackQueryHandler)
from src.components import commands
import os
import dotenv


dotenv.load_dotenv()
DEBUG = os.environ.get('DEBUG', False) == 'True'


def main():
    updater = Updater(os.environ['BOT_TOKEN'])
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', commands.start))

    updater.start_polling()
    updater.idle()
