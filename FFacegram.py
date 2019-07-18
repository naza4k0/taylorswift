import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from pyre import Pyre
import logging
import random

def start(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Send your score in a format \n -name- -type- -score-. \n For example, \n -Iron Man- -Movie- -10-")

def text_upd(bot, update):
        bot.forward_message(chat_id = 367989051, from_chat_id=update.message.chat_id, message_id=update.message.message_id)
        bot.send_message(chat_id=update.message.chat_id, text="Thank you for your score. It will be added to the system soon.")

def photo_upd(bot, update):
        bot.forward_message(chat_id = 367989051, from_chat_id=update.message.chat_id, message_id=update.message.message_id)
        bot.send_message(chat_id=update.message.chat_id, text="Thank you for your score. It will be added to the system soon.")
    
updater = Updater(token='922359953:AAEBvc5uRRO7qMPD6CI8TgdtHHz-oev42uQ')
dispatcher = updater.dispatcher

echo2_handler = MessageHandler(Filters.photo, photo_upd)
dispatcher.add_handler(echo2_handler)

echo1_handler = MessageHandler(Filters.text, text_upd)
dispatcher.add_handler(echo1_handler)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
