import telebot

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start','help'])
def start_and_help(message):
    bot.reply_to(message,"Hi!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()