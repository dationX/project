import telebot
from telebot import types

bot = telebot.TeleBot("7596207695:AAEAu1v793a25x18ZpQzWNzRkQxhgD3ztXY")

names_button = ["Обработать твои привычки и рассчитать углеродный след", "Предоставить советы"]
habits = {"Использование автомобилей": 4.6, "Расжигание костров": 2, "Потребление мяса": 7.2,
          "Использование угля для отопления": 3.5, "Высокий уровенеь потребления энергии": 2,
          "Неэффективное использование воды": 0.4, "Отказ от переработки (мусора, например)": 1,
          "Потребление пластиковых изделий": 1, "Частые авиаперелеты": 3, "Увлечение модой (одежда в большом количестве)": 5,
          "Увлечение высокими технологиями (при частой замене электроники)": 0.75, "Покупка товаров с большим количеством упаковки": 1,
          "Вырубка лесов": 20, "Потребление топлива в неэффективных транспортных средствах": 6,
          "Использование старой бытовой техники": 1.5, "Поддержание большого домашнего хозяйства": 4,
          "Практика неорганического земледелия": 2, "Частые поездки на дачу или в загородные дома": 2,
          "Игнорирование энергосберегающих решений": 1.5, "Использование жиженого газа": 1.5,
          "Отказ от использований солнечных панелей": 2.5, "Чрезмерное потребление воды в быту": 0.35,
          "Отказ от реставраций старой мебели": 0.75, "Обслуживание старого транспорта": 3.5, 
          "Промышлеенная перееработка без утилизации": 4.5, "Неэффективноеее отопление зданий": 3,
          "Частая замена одежды": 4, "Покупка экзотических фруктов и овощей": 0.6, "Увлечение курением": 1.5,
          "Увлечение фаст-фудом": 7.5}

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

@bot.message_handler(content_types=['text'])
def processing_button(message):
    if message.text == "Обработать твои привычки и рассчитать углеродный след":
        message_habits = ""
        count = 0

        for habit in habits.keys():
            count += 1
            message_habits += f"{count}) {habit}\n"
        
        bot.send_message(message.chat.id, message_habits)
        bot.send_message(message.chat.id,
"""
Напишите номера ваших привычек из этого списка через запятую, пример: 1,6,9,15
"""
)
        bot.register_next_step_handler(message, save_habits)
    elif message.text == "Предоставить советы":
        pass
        
    
def save_habits(message):
    try:

        chat_id = message.chat.id
        text_user = message.text
        habits_user = text_user.split(",")

        co2_user = 0

        for habit in habits_user:
            co2_user += habits[list(habits.keys())[int(habit)-1]]

        bot.send_message(chat_id, f"Вы выбрасывате в год примерно {co2_user} тонн углекислого газа в год")

        if co2_user <= 2:
            dop_message = "Отлично"
        elif co2_user >= 2 and co2_user <= 5:
            dop_message = "Хорошо"
        elif co2_user >= 5 and co2_user <= 10:
            dop_message = "Следует задуматься!"
        elif co2_user >= 10 and co2_user <= 15:
            dop_message = "Пора принимать меры!"
        elif co2_user >= 15:
            dop_message = "Критическая ситуация"

        bot.send_message(chat_id, f"Оценка вашего результата: {dop_message}")
    except:
        pass

bot.polling()
