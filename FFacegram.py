import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from pyre import Pyre
import logging
import random

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Привет, используй комманду /girls для того чтобы принять участие в голосовании")


def girls(bot, update):
    girls2(bot, update.message.chat_id)

def rating(bot, update):
    rates = Pyre().rating()
    textr = "🥇 : " + Pyre().name(rates[0]) + "\n" + "🥈 : " + Pyre().name(rates[1]) + "\n" + "🥉 : " + Pyre().name(rates[2]) + "\n" + "👩 : " + Pyre().name(rates[3]) + "\n" + "👩 : " + Pyre().name(rates[4])
    bot.send_message(chat_id=update.message.chat_id, text=textr)

def girls2(bot, chat_id):
    a=0
    b=0

    while a==b:
       a=random.randint(0,14)
       b=random.randint(0,14)

    x = bot.send_photo(chat_id=chat_id, photo=Pyre().photo(a)).message_id
    y = bot.send_photo(chat_id=chat_id, photo=Pyre().photo(b)).message_id
    bot.send_message(chat_id=chat_id, text="Какая девушка лучше?", reply_markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text="Верхняя", callback_data= f'{a} {b} {x} {y}'), InlineKeyboardButton(text="Нижняя", callback_data=f'{b} {a} {x} {y}')]]))
   
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
rating_handler = CommandHandler('rating', rating)
dispatcher.add_handler(girls_handler)
dispatcher.add_handler(rating_handler)
updater.dispatcher.add_handler(CallbackQueryHandler(handle_query))
updater.start_polling()
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)
