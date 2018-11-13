import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from pyre import Pyre
import logging
import random

def from_super_admin(update):
    super_admins_ids = [367989051]
    return (update.message.from_user.id in super_admins_ids)

def from_admins(update):
    admins_ids = [233768128, 364448153, 330954316]
    return (from_super_admin(update) or (update.message.from_user.id in admins_ids))

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

def m_vote(bot, update):
    m_vote2(bot, update.message.chat_id)

def g_nrating(bot, update):
    rates = Pyre().g_rating()
    girls_number = 5
    emojis = ['🥇', '🥈', '🥉', '👩‍', '👩‍']
    girls_titles = [Pyre().g_link(rates[i]) for i in range(girls_number)]
    textr = '\n'.join([f'{e} : {name_with_link}' for e, name_with_link in zip(emojis, girls_titles)])
    bot.send_message(chat_id=update.message.chat_id, text=textr, parse_mode="HTML", disable_web_page_preview=True)

def m_nrating(bot, update):
    rates = Pyre().m_rating()
    men_number = 5
    emojis = ['🥇', '🥈', '🥉', '👦🏻', '👦🏻']
    girls_titles = [Pyre().m_link(rates[i]) for i in range(men_number)]
    textr = '\n'.join([f'{e} : {name_with_link}' for e, name_with_link in zip(emojis, girls_titles)])
    bot.send_message(chat_id=update.message.chat_id, text=textr, parse_mode="HTML", disable_web_page_preview=True)

def g_idrating(bot, update):
    Pyre().reg_check(update.message.chat_id)
    rates = Pyre().gid_rating(update.message.chat_id)
    girls_number = 5
    emojis = ['🥇', '🥈', '🥉', '👩‍', '👩‍']
    girls_titles = [Pyre().g_link(rates[i]) for i in range(girls_number)]
    textr = '\n'.join([f'{e} : {name_with_link}' for e, name_with_link in zip(emojis, girls_titles)])
    bot.send_message(chat_id=update.message.chat_id, text=textr, parse_mode="HTML", disable_web_page_preview=True)

def m_idrating(bot, update):
    Pyre().mreg_check(update.message.chat_id)
    rates = Pyre().mid_rating(update.message.chat_id)
    men_number = 5
    emojis = ['🥇', '🥈', '🥉', '👦🏻', '👦🏻']
    girls_titles = [Pyre().m_link(rates[i]) for i in range(men_number)]
    textr = '\n'.join([f'{e} : {name_with_link}' for e, name_with_link in zip(emojis, girls_titles)])
    bot.send_message(chat_id=update.message.chat_id, text=textr, parse_mode="HTML", disable_web_page_preview=True)

def g_adrating(bot, update):
    if from_admins(update):
        rates = Pyre().g_admin_rating()
        rating_list_text = '\n'.join([f'{i+1}. {Pyre().g_name(rate)}' for i, rate in enumerate(rates)])
        bot.send_message(chat_id=update.message.chat_id, text=rating_list_text)
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Sorry, you need admin rights to do that.")

def m_adrating(bot, update):
    if from_admins(update):
        rates = Pyre().m_admin_rating()
        rating_list_text = '\n'.join([f'{i+1}. {Pyre().m_name(rate)}' for i, rate in enumerate(rates)])
        bot.send_message(chat_id=update.message.chat_id, text=rating_list_text)
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
    d = 1
    bot.send_message(chat_id=chat_id, text="Какая девушка лучше? 🍓　　　", reply_markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text="Левая", callback_data= f'{a} {b} {x1} {x2} {d}'), InlineKeyboardButton(text="Правая", callback_data=f'{b} {a} {x1} {x2} {d}')]]))
   
def m_vote2(bot, chat_id):
    a=0
    b=0

    while a==b or abs(Pyre().m_score(a)-Pyre().m_score(b))>=100:
       a=random.randint(0,Pyre().m_number()-1)
       b=random.randint(0,Pyre().m_number()-1)

    media = [telegram.InputMediaPhoto(Pyre().m_photo(a)), telegram.InputMediaPhoto(Pyre().m_photo(b))]
    x = bot.send_media_group(chat_id=chat_id, media=media)
    x1 = x[0].message_id
    x2 = x[1].message_id
    print(x)
    d = 0
    bot.send_message(chat_id=chat_id, text="Какой парень лучше? 🍆　　　", reply_markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text="Левый", callback_data= f'{a} {b} {x1} {x2} {d}'), InlineKeyboardButton(text="Правый", callback_data=f'{b} {a} {x1} {x2} {d}')]]))
   
def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

def handle_query(bot, update):
    data = update.callback_query.data
    a, b, x1, x2, d = data.split()
    c = update.callback_query.message.chat.id
    bot.delete_message(c,x1)
    bot.delete_message(c,x2)
    update.callback_query.message.delete()
    if d == '1':
        Pyre().reg_check(c)
        Pyre().g_round(a, b)
        Pyre().g1_round(a, b, c)
        g_vote2(bot, c)
    else:
        Pyre().mreg_check(c)
        Pyre().m_round(a, b)
        Pyre().m1_round(a, b, c)
        m_vote2(bot, c)
    
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
idrating_handler = CommandHandler('irating', g_idrating)
adrating_handler = CommandHandler('admin_rating', g_adrating)

mgirls_handler = CommandHandler('mvote', m_vote)
mrating_handler = CommandHandler('mrating', m_nrating)
midrating_handler = CommandHandler('mirating', m_idrating)
madrating_handler = CommandHandler('madmin_rating', m_adrating)

dispatcher.add_handler(adrating_handler)
dispatcher.add_handler(girls_handler)
dispatcher.add_handler(rating_handler)
dispatcher.add_handler(idrating_handler)

dispatcher.add_handler(madrating_handler)
dispatcher.add_handler(mgirls_handler)
dispatcher.add_handler(mrating_handler)
dispatcher.add_handler(midrating_handler)

updater.dispatcher.add_handler(CallbackQueryHandler(handle_query))
updater.start_polling()

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)
