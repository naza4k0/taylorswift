import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from pyre import Pyre
import logging
import random

def from_super_admin(update):
    super_admins_ids = [367989051]
    update.message.from_user.id in super_admins_ids

def from_admins(update):
    admins_ids = [233768128, 364448153, 330954316]
    from_super_admin(update) or update.message.from_user.id in admins_ids

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Привет, используй комманду /vote для того чтобы принять участие в голосовании")

def text_upd(bot, update):
    if from_super_admin(update):
        Pyre().g_text_upload(update.message.text)
    else:
        bot.forward_message(chat_id = 367989051, from_chat_id=update.message.chat_id, message_id=update.message.message_id)

def photo_upd(bot, update):
    if from_super_admin(update):
        Pyre().g_photo_upload(update.message.photo[0].file_id)
    else:
        bot.forward_message(chat_id = 367989051, from_chat_id=update.message.chat_id, message_id=update.message.message_id)
        
def g_vote(bot, update):
    g_vote2(bot, update.message.chat_id)

def g_nrating(bot, update):
    rates = Pyre().g_rating()
    girls_number = 10
    emojis = ['🥇', '🥈', '🥉', '💛', '💛', '💚', '💚', '💚', '💚', '💚']
    girls_titles = [Pyre().g_name(rates[i]) + Pyre().g_link(rates[i]) for i in range(girls_number)]
    textr = '\n'.join([f'{e} : {name_with_link}' for e, name_with_link in zip(emojis, girls_titles)])
    bot.send_message(chat_id=update.message.chat_id, text=textr, parse_mode="HTML", disable_web_page_preview=True)

def g_adrating(bot, update):
    if from_admins(update):
        rates = Pyre().g_admin_rating()
        rating_list_text = '\n'.join([f'{i+1}. {Pyre().g_name(rate)}' for i, rate in enumerate(rates)])
        bot.send_message(chat_id=update.message.chat_id, text=rating_list_text)
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Sorry, you need admin rights to do that.")

def update(bot, update):
    if from_super_admin(update):
        Pyre().g_updater()
        bot.send_message(chat_id=update.message.chat_id, text="Update successful.")
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Sorry, you need admin rights to do that.")

def g_vote2(bot, chat_id):
    a=0
    b=0

    while a==b or abs(Pyre().g_score(a)-Pyre().g_score(b))>=100:
       a=random.randint(0,Pyre().g_number()-1)
       b=random.randint(0,Pyre().g_number()-1)

    media = [telegram.InputMediaPhoto(Pyre().g_photo(a)), telegram.InputMediaPhoto(Pyre().g_photo(b))]
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
    Pyre().g_round(a, b)
    g_vote2(bot, c)
    
updater = Updater(token='757304961:AAFFLGinPle1bE5Arq12SL2mFiGj_DL849E')
dispatcher = updater.dispatcher

echo2_handler = MessageHandler(Filters.photo, photo_upd)
dispatcher.add_handler(echo2_handler)

echo1_handler = MessageHandler(Filters.text, text_upd)
dispatcher.add_handler(echo1_handler)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

girls_handler = CommandHandler('vote', g_vote)
rating_handler = CommandHandler('rating', g_nrating)
updater_handler = CommandHandler('update', update)
adrating_handler = CommandHandler('admin_rating', g_adrating)

dispatcher.add_handler(adrating_handler)
dispatcher.add_handler(updater_handler)
dispatcher.add_handler(girls_handler)
dispatcher.add_handler(rating_handler)

updater.dispatcher.add_handler(CallbackQueryHandler(handle_query))
updater.start_polling()

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)
