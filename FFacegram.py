import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from pyre import Pyre
import logging
import random

def from_admin(update):
        admins_ids = [367989051]
        return (update.message.from_user.id in admins_ids)

def start(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Send your audio you want to add to the library or use the command /music to get a random track from it.")

def text_upd(bot, update):
        bot.forward_message(chat_id = 367989051, from_chat_id=update.message.chat_id, message_id=update.message.message_id)
        
def music_upd(bot, update):
        if from_admin(update):
                Pyre().music_upload(update.message.audio.file_id)
        else:
                bot.forward_message(chat_id = 367989051, from_chat_id=update.message.chat_id, message_id=update.message.message_id)

def music_send(bot, update):
        rand_music = random.randint(1,Pyre().num_get())
        music = Pyre().music_get(rand_music)

        bot.send_audio(chat_id = update.message.chat_id, audio=music)

updater = Updater(token='1053633256:AAEphnCCmpK9-J9cVgnLcExOol1_w5wzEZY')
dispatcher = updater.dispatcher

echo2_handler = MessageHandler(Filters.audio, music_upd)
dispatcher.add_handler(echo2_handler)

echo1_handler = MessageHandler(Filters.text, text_upd)
dispatcher.add_handler(echo1_handler)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

music_handler = CommandHandler('music', music_send)
dispatcher.add_handler(music_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
