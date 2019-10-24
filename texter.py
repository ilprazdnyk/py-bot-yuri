def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
