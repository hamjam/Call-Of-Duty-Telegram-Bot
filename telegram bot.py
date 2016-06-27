from telegram.ext import Updater, Dispatcher, CommandHandler, MessageHandler
from telegram import message, sticker, emoji, bot


def main():
    updater = Updater(token='205572739:AAEFs_y41exvonAdtj_ZHV9koxdzRrd7nz4')

    dispatcher = updater.dispatcher
    myBot = bot.Bot(token='205572739:AAEFs_y41exvonAdtj_ZHV9koxdzRrd7nz4')
    while True:
        myBot.sendMessage(updtext='Hi')
    updater.start_polling()
main()
