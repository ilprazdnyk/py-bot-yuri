# a simple callback function for the message handler, which counts number of symbols in a new message
#the goal is to extend it so it would pass a new update as an input into gpt-2 and send output as a message
def echo(update, context):
    sentence = update.message.text
    result = len(sentence)

    context.bot.send_message(chat_id=update.effective_chat.id, text=result)
