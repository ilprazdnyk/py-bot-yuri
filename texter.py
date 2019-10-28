def echo(update, context):
    sentence = update.message.text
    result = len(sentence)

    context.bot.send_message(chat_id=update.effective_chat.id, text=result)
