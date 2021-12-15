from logging import DEBUG
from telegram.ext import (Updater,
                          CommandHandler,
                          ConversationHandler)
from src.components import commands, start
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

    main_conversation = ConversationHandler(
        entry_points=[
            CommandHandler('start', start.start)
        ],
        states={

        },
        fallbacks=[
            CommandHandler('help', commands.help),
        ]
    )

    dispatcher.add_handler(main_conversation)

    updater.start_polling()
    updater.idle()
