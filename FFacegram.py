import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from pyre import Pyre
import logging
import random

photos = {
    0 : "AgADAgADlakxG9prGEsbKi4dUy2IfmD99A4ABHnZPhY0G_sgm3sAAgI",
    1 : "AgADAgADlKkxG9prGEtIFhsH_cHKElOiOQ8ABLP4Di4twYXc90gAAgI",
    2 : "AgADAgADpakxG9prGEvXcoF-wd4VG4G0tw4ABFkE9zwoXMg4YTgGAAEC"
}

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Привет, используй комманду /girls для того чтобы принять участие в голосовании")


def girls(bot, update):
    girls2(bot, update.message.chat_id)

def girls2(bot, chat_id):
    a=0
    b=0

    while a==b:
       a=random.randint(0,2)
       b=random.randint(0,2)

    x = bot.send_photo(chat_id=chat_id, photo=photos[a]).message_id
    y = bot.send_photo(chat_id=chat_id, photo=photos[b]).message_id
    bot.send_message(chat_id=chat_id, text="Какая топовее?", reply_markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text="Первая", callback_data= f'{a} {b} {x} {y}'), InlineKeyboardButton(text="Вторая", callback_data=f'{b} {a} {x} {y}')]]))
   
def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

def handle_query(bot, update):
    data = update.callback_query.data
    a, b, x, y = data.split()
    c = update.callback_query.message.chat.id
    bot.delete_message(c,x)
    bot.delete_message(c,y)
    update.callback_query.message.delete()
    Pyre().increment(a, b)
    girls2(bot, c)
    
updater = Updater(token='757304961:AAFFLGinPle1bE5Arq12SL2mFiGj_DL849E')

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

girls_handler = CommandHandler('girls', girls)
dispatcher.add_handler(girls_handler)
updater.dispatcher.add_handler(CallbackQueryHandler(handle_query))

updater.start_polling()

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)
