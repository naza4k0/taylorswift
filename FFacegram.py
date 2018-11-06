from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Привет, используй комманду /girls для того чтобы принять участие в голосовании")


def girls(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Го сэкс")


def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")


updater = Updater(token='757304961:AAFFLGinPle1bE5Arq12SL2mFiGj_DL849E')

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

girls_handler = CommandHandler('girls', girls)
dispatcher.add_handler(girls_handler)

updater.start_polling()

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)