#Having hard time to extend this function, i will have to read the documentation
def echo(update, context): #this funcion is going to be executed once bot gets a new message
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
