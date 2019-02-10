import telebot
import time

TOKEN = '655696633:AAEu2azozVNfEGBG8A1XilciQpyTd0j6lpI'
bot = telebot.TeleBot(token=TOKEN)

GAMES = ['AD', 'APEX', 'RB6', 'BDO', 'D2', 'MHW', 'ANTHEM']
USERS = { 
    'JOMARK' : 323943026, 
    'JASON' : 000, 
    'ERBERT' : 64444894,
    'TOFFEE' : 299512266
}
ROLES = {
    'AD': ['JOMARK', 'TOFFEE', 'GLENN']
}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome!')


@bot.message_handler(commands=['tag'])
def tag_players(message):
    command = message.text.split(' ')
    if command[1] == 'AD':
        bot.send_message(message.chat.id, '@johnnotdoe')
    else:
        bot.send_message(message.chat.id, 'Hmmm')

@bot.message_handler(commands=['tag_all'])
def tag_all(message):
    bot.get_chat_member(message.chat.id, 323943026)

bot.polling()