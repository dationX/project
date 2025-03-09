import telebot
from telebot import types

bot = telebot.TeleBot("YOUR TOKEN")

names_button = ["Обработать твои привычки", "Рассчитать углеродный след", "Предоставить советы"]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
"""
Привет! Я Telegram бот, который поможет тебе меньше выделять углекислый газ.
Если ты хочешь узнать, что я умею, то пропиши: /button.
""")

@bot.message_handler(commands="button")
def func_keyboard(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    for name_button in names_button:
        markup.add(name_button)

    bot.send_message(message.chat.id, "Что я умею: ", reply_markup=markup)
    
bot.polling()
