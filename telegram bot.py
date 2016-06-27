from telegram.ext import Updater, Dispatcher, CommandHandler, MessageHandler
from telegram import message, sticker, emoji, bot


def main():
    updater = Updater(token='179409747:AAFMOpkXpZLQcqjVVlzvIl4FidpFJ1z75I0')

    dispatcher = updater.dispatcher
    myBot = bot.Bot(token='179409747:AAFMOpkXpZLQcqjVVlzvIl4FidpFJ1z75I0')
    while True:
        myBot.sendMessage(updtext='Hi')
    updater.start_polling()
main()
