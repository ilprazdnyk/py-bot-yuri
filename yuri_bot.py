import logging
import weather
import time
import mnist_model
import os
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
import dialogflow_v2 as dialogflow


token = '*Token from BotFather'
updater = Updater(token=token, use_context=True)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! My name is Yuri, I am glad to help you")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


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


DIALOGFLOW_PROJECT_ID = '*Project id of Dialogflow Agent'
DIALOGFLOW_LANGUAGE_CODE = 'en-US'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '*JSON key from dialogflow*'
SESSION_ID = '*Come up with session name*'
session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)


def yuri_response(update, context):
    print(update.message)
    received_text = update.message.text
    text_input = dialogflow.types.TextInput(text=received_text, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response_intent = session_client.detect_intent(session=session, query_input=query_input)
    print(response_intent.query_result)
    response = response_intent.query_result.fulfillment_text
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)


text_handler = MessageHandler(Filters.text, yuri_response)
dispatcher.add_handler(text_handler)


def photo_get(update, context):

    context.bot.send_message(chat_id=update.effective_chat.id, text='Image received, digit recognition mode activated')
    photo_id = update.message.photo[-1]['file_id']
    new_photo = context.bot.get_file(photo_id)
    new_photo.download('pic.jpg')
    time.sleep(3)
    context.bot.send_message(chat_id=update.effective_chat.id, text='Image downloaded to the server')
    time.sleep(1)
    context.bot.send_message(chat_id=update.effective_chat.id, text='Calculating...')
    time.sleep(1)
    result = 'The prediction is: ' + mnist_model.do_prediction()
    context.bot.send_message(chat_id=update.effective_chat.id, text=result)


img_handler = MessageHandler(Filters.photo, photo_get)
dispatcher.add_handler(img_handler)

updater.start_polling()