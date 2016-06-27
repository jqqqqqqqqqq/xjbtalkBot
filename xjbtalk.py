import telebot
import random

bot = telebot.TeleBot("224142514:AAH7bfxWs6G9L4BSqK-VQ3HzJlJVE7TaKFE")

@bot.message_handler(commands=['start','help'])
def start_and_help(message):
    # bot.reply_to(message,"Hi!")
    bot.send_message(message.chat.id,"hello")


@bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain')
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()