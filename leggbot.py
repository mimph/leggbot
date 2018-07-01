#!/usr/bin/python3

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import choice

# initial setup
updater = Updater(token='592889292:AAH8Cbe_PcmRweQSkWxHPcPVXRWrzEkUH6E')
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# adding functionality
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Geaaagh! I'm the legg bot. My purpose is to give you a silly answer, that sounds like an upset seal.")

def legg(bot, update):
    items = ['legg', 'mimph', 'AAAA', 'murph', 'fibsh', 'liggk']
    item = choice(items)
    bot.send_message(chat_id=update.message.chat_id, text=item)

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand. Mimph!")

start_handler = CommandHandler('start', start)
legg_handler = MessageHandler(Filters.text, legg)
unknown_handler = MessageHandler(Filters.command, unknown)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(legg_handler)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
