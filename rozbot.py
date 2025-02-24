import telebot
from telebot import types

# Введіть свій токен, отриманий від BotFather
TOKEN = '7881434050:AAGNmy4roLSFg6e4R0ENisP-ZwLDeLfEoJI'
bot = telebot.TeleBot(TOKEN)

# Розклад уроків
schedule = {
    'понеділок': [
        '1. Українська мова',
        '2. Географія',
        '3. Математика',
        '4. Фізкультура',
        '5. Пізнаємо природу',
        '6. Історія України. Всесвітня іторія'
    ],
    'вівторок': [
        '1. Математика',
        '2. Зарубіжна література',
        '3. Українська література',
        '4. Географія',
        '5. Англійська мова',
        '6. Здоров’я, безпека та добробут'
    ],
    'середа': [
        '1. Англійська мова',
        '2. Українська мова',
        '3. Математика',
        '4. Фізкультура',
        '5. Історія України. Всесвітня історія.',
        '6. Мистецтво: музичне мистецтво',
        '7. /Інформатика'
    ],
    'четвер': [
        '1. Англійська мова',
        '2. Українська мова',
        '3. Математика',
        '4. Пізнаємо природу',
        '5. Технології',
        '6. Технології',
        '7. Технології'
    ],
    'п’ятниця': [
        '1. Українська мова',
        '2. Математика',
        '3. Фізкультура',
        '4. Англійська мова',
        '5. Образотворче мистецтво',
        '6. Інформатика'
    ]
}

# Команда /start
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ['понеділок', 'вівторок', 'середа', 'четвер', 'п’ятниця']
    markup.add(*[types.KeyboardButton(day) for day in buttons])
    bot.send_message(message.chat.id, "Привіт! Я бот з розкладом уроків для 6-А класу. Оберіть день тижня:", reply_markup=markup)

# Відображення розкладу
@bot.message_handler(func=lambda message: message.text in schedule.keys())
def show_schedule(message):
    day = message.text
    lessons = schedule.get(day, [])
    if lessons:
        bot.send_message(message.chat.id, f"Розклад на {day}:\n" + "\n".join(lessons))
    else:
        bot.send_message(message.chat.id, "Розклад на цей день відсутній.")

# Запуск бота
bot.polling(none_stop=True)
