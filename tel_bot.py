from telegram import *
from telegram.ext import *
from requests import *

updater = Updater(token = "5814474945:AAE1dBV1Gi1x1ls_j1loP7cBqdna_3jSnf0")
dispatcher = updater.dispatcher

randomImageText = 'Random Image'
randomPImageURL = 'https://picsum.photos/1200'

def startCommand(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton('Random Image')]]
    context.bot.send_message(chat_id=update.effective_chat.id, text='Welcome my little friend :)',
    reply_markup=ReplyKeyboardMarkup(buttons))

def messageHandler(update: Update, context: CallbackContext):
    if randomImageText in update.message.text:
        image = get(randomPImageURL).content
    if image:
        context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[InputMediaPhoto(image, caption="")])

dispatcher.add_handler(CommandHandler('start', startCommand))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))

updater.start_polling()
