import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from pyre import Pyre
import logging
import random

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Привет, используй комманду /vote для того чтобы принять участие в голосовании")

def nazar1(bot, update):
    if update.message.from_user.id == 367989051:
        b = update.message.text
        Pyre().adminka1(b)
    else:
        b = update.message.text
        a = str(update.message.from_user.id) + ": " + update.message.from_user.first_name + " " + update.message.from_user.last_name + ", " + update.message.from_user.username
        bot.send_message(chat_id=367989051, text= a + "\n" + b)

def nazar2(bot, update):
    if update.message.from_user.id == 367989051:
        b = update.message.photo[0].file_id
        Pyre().adminka2(b)
    else:
        b = update.message.photo[0].file_id
        a = str(update.message.from_user.id) + ": " + update.message.from_user.first_name + " " + update.message.from_user.last_name + ", " + update.message.from_user.username
        bot.send_photo(chat_id=367989051, photo=b)
        bot.send_message(chat_id=367989051, text=a)
        
def vote_girls(bot, update):
    vote_girls2(bot, update.message.chat_id)

def rating(bot, update):
    rates = Pyre().rating()
    textr = "🥇 : " + Pyre().name(rates[0]) + "\n" + "🥈 : " + Pyre().name(rates[1]) + "\n" + "🥉 : " + Pyre().name(rates[2]) + "\n" + "👩 : " + Pyre().name(rates[3]) + "\n" + "👩 : " + Pyre().name(rates[4])
    bot.send_message(chat_id=update.message.chat_id, text=textr)

def adrating(bot, update):
    if update.message.from_user.id == 367989051:
        rates = Pyre().admin_rating()
        textr = ""
        for i in range(len(rates)):
            textr += str(i+1)
            textr += ". "
            textr += Pyre().name(rates[i])
            textr += "\n"
        bot.send_message(chat_id=update.message.chat_id, text=textr)
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Sorry, you need admin rights to do that.")

def update(bot, update):
    if update.message.from_user.id == 367989051:
        Pyre().updater()
        bot.send_message(chat_id=update.message.chat_id, text="Update successful.")
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Sorry, you need admin rights to do that.")

def vote_girls2(bot, chat_id):
    a=0
    b=0

    while a==b:
       a=random.randint(0,Pyre().num_get()-1)
       b=random.randint(0,Pyre().num_get()-1)

    media = [telegram.InputMediaPhoto(Pyre().photo(a)), telegram.InputMediaPhoto(Pyre().photo(b))]
    x = bot.send_media_group(chat_id=chat_id, media=media)
    x1 = x[0].message_id
    x2 = x[1].message_id
    print(x)
    bot.send_message(chat_id=chat_id, text="Какая девушка лучше? 🍓　　　", reply_markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text="Левая", callback_data= f'{a} {b} {x1} {x2}'), InlineKeyboardButton(text="Правая", callback_data=f'{b} {a} {x1} {x2}')]]))
   
def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

def handle_query(bot, update):
    data = update.callback_query.data
    a, b, x1, x2= data.split()
    c = update.callback_query.message.chat.id
    bot.delete_message(c,x1)
    bot.delete_message(c,x2)
    update.callback_query.message.delete()
    Pyre().increment(a, b)
    vote_girls2(bot, c)
    
updater = Updater(token='757304961:AAFFLGinPle1bE5Arq12SL2mFiGj_DL849E')
dispatcher = updater.dispatcher

echo2_handler = MessageHandler(Filters.photo, nazar2)
dispatcher.add_handler(echo2_handler)
echo1_handler = MessageHandler(Filters.text, nazar1)
dispatcher.add_handler(echo1_handler)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
girls_handler = CommandHandler('vote', vote_girls)
rating_handler = CommandHandler('rating', rating)
updater_handler = CommandHandler('update', update)
adrating_handler = CommandHandler('admin_rating', adrating)
dispatcher.add_handler(adrating_handler)
dispatcher.add_handler(updater_handler)
dispatcher.add_handler(girls_handler)
dispatcher.add_handler(rating_handler)
updater.dispatcher.add_handler(CallbackQueryHandler(handle_query))
updater.start_polling()
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)
