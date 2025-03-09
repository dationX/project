import telebot

token = "YOUR TOKEN"
bot = telebot.Telebot(token)

@bot.message_handler(commands=['start'])
def start_message(message)
  bot.send_message()

bot.infinity_polling()
