from logging import DEBUG
from telegram.ext import (Updater,
                          CommandHandler,
                          CallbackQueryHandler)
from src.components import commands
import os
import dotenv
import logging


dotenv.load_dotenv()
DEBUG = os.environ.get('DEBUG', False) == 'True'


logging.basicConfig(
    filename='logs.log' if not DEBUG else None,
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG if DEBUG else logging.INFO
)

logger = logging.getLogger(__name__)


def main():
    updater = Updater(os.environ['BOT_TOKEN'])
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', commands.start))

    updater.start_polling()
    updater.idle()
