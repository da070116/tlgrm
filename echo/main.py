from telegram import Bot
from telegram import Update
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Updater, Filters

from echo.config import TLGRM_TOKEN


def do_start(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Greet message'
    )


def do_echo(bot: Bot, update: Update):
    text = update.message.text
    chat_identifier = update.message.chat_id
    bot.send_message(
        chat_id=chat_identifier,
        text=f'You are {chat_identifier} and you wrote me: "{text}"'
    )


def main():
    bot = Bot(
        token=TLGRM_TOKEN,
    )
    updater = Updater(
        bot=bot,
    )
    start_handler = CommandHandler('start', do_start)
    msg_handler = MessageHandler(Filters.text, do_echo)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(msg_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
