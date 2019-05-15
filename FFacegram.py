import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from pyre import Pyre
import logging
import random

def start(bot, update):
       bot.send_message(chat_id=update.message.chat_id, text="Send anything you would like to ask or to talk to here.")

def text_upd(bot, update):
       bot.forward_message(chat_id = 367989051, from_chat_id=update.message.chat_id, message_id=update.message.message_id)
       bot.send_message(chat_id=update.message.chat_id, text="Thank you, for your message, it will be answered any time soon.")

def photo_upd(bot, update):
       bot.forward_message(chat_id = 367989051, from_chat_id=update.message.chat_id, message_id=update.message.message_id)
       bot.send_message(chat_id=update.message.chat_id, text="Thank you, for your message, it will be answered any time soon.")
    
updater = Updater(token='897701785:AAGw54uyE4L2Zo3st1lJC11tRKDXwGbBQrY')
dispatcher = updater.dispatcher

echo2_handler = MessageHandler(Filters.photo, photo_upd)
dispatcher.add_handler(echo2_handler)

echo1_handler = MessageHandler(Filters.text, text_upd)
dispatcher.add_handler(echo1_handler)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.dispatcher.add_handler(CallbackQueryHandler(handle_query))
updater.start_polling()

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)
