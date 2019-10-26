#importing libraries
import logging
import weather
from texter import echo
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

#setting the bot token into container
updater = Updater(token='842440069:AAGNacGGPSgufJmJgeyCo29sB-zMp5vsp9Q', use_context=True)
#the wrapper for the bot uses logging library which needs setting to special format
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
dispatcher = updater.dispatcher

#defenition of the function which is going to be called after someone 
#starts the dialogue with the bot or types the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

#now we have to make a command handler from that function and add it to the dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()

#defenition of the function which is going to be called after someone 
#types the /temp command, the source is weather.py script
def temp(update, context):
    weather_text = weather.prague_weather()
    context.bot.send_message(chat_id=update.effective_chat.id, text=weather_text)

#now just like with the start command we have to make a handler from this one and add it to the dispatcher
temp_handler = CommandHandler('temp', temp)
dispatcher.add_handler(temp_handler)

#the defenition of a caps function, just like with the prvious ones
def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

#and now creation and activation of the handler, same as before
caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)


def master(update, context):
    text = ' https://www.reddit.com/r/blackmagicfuckery/comments/b32e3o/pole_master/' \
           '?utm_source=share&utm_medium=ios_app&utm_name=iossmf'
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


master_handler = CommandHandler('master', master)
dispatcher.add_handler(master_handler)

# The handler is in a separate script texter.py


echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
