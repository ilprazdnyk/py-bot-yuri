import logging
import weather
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

updater = Updater(token='842440069:AAGNacGGPSgufJmJgeyCo29sB-zMp5vsp9Q', use_context=True)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()


def temp(update, context):
    weather_text = weather.prague_weather()
    context.bot.send_message(chat_id=update.effective_chat.id, text=weather_text)


temp_handler = CommandHandler('temp', temp)
dispatcher.add_handler(temp_handler)


def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)


def master(update, context):
    text = ' https://www.reddit.com/r/blackmagicfuckery/comments/b32e3o/pole_master/' \
           '?utm_source=share&utm_medium=ios_app&utm_name=iossmf'
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


master_handler = CommandHandler('master', master)
dispatcher.add_handler(master_handler)
