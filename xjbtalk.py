import telebot
import random

bot = telebot.TeleBot("224142514:AAH7bfxWs6G9L4BSqK-VQ3HzJlJVE7TaKFE")

@bot.message_handler(commands=['start','help'])
def start_and_help(message):
    # bot.reply_to(message,"Hi!")
    bot.send_message(message.chat.id,"hello")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

@bot.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    try:
        r = telebot.types.InlineQueryResultArticle('1', 'Result', telebot.types.InputTextMessageContent('Result message.'))
        r2 = telebot.types.InlineQueryResultArticle('2', 'Result2', telebot.types.InputTextMessageContent('Result message2.'))
        #r3 = telebot.types.InlineQueryResultArticle('3', 'Custom', telebot.types.InputTextMessageContent(str(inline_query.location.latitude) + ', '+str(inline_query.location.longtitude)))
        print inline_query.__dict__
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)


bot.polling()