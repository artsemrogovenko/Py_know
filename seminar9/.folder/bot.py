
#скачиваем библиотеку pip install pytelegrambotapi
# python -m имяОкружения .venv
import telebot
from telebot import types

user_sweets = 0
sweets= 221
bot = telebot.TeleBot("5975082909:AAH4Y1jLdlU-yBA2nvfImBgFvXWFg1C0bV0")
@bot.message_handler(commands = ['start'])#вызов функции по команде в списке
def start(message):
    global sweets
    bot.send_message(message.chat.id,f"Введите количество не больше 28")#отправка сообщения (кому отправляем, что отправляем(str))
    bot.register_next_step_handler(message,user_input)
    
def get_count(message):
    global sweets
    sweets=sweets-user_sweets
    bot.send_message(message.chat.id,f"осталось {sweets}")
    start(message)

def user_input(message):
    global user_sweets
    user_sweets = int(message.text)
    get_count(message)


# @bot.message_handler(commands=['start'])  # вызов функции по команде в списке
# def start(message):
#         # отправка сообщения (кому отправляем, что отправляем(str))
#     bot.send_message(message.chat.id, f"/button")
#     print(user_sweets)


# def summa(message):
#     summ = sum(list(map(int, message.text.split())))
#     bot.send_message(message.chat.id, str(summ))
#     button(message)


# @bot.message_handler(commands=["button"])
# def button(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание клавиатуры
#     but1 = types.KeyboardButton("сумма")  # создание кнопок
#     but2 = types.KeyboardButton("разность")
#     markup.add(but1)  # добавление кнопок
#     markup.add(but2)  # добавление кнопок
#     bot.send_message(message.chat.id, "Выбери ниже", reply_markup=markup)


# # вызов функции если тип сообщения - текст
# @bot.message_handler(content_types=["text"])
# def controller(message):
#     if message.text == "сумма":
#         bot.send_message(message.chat.id, "введи два числа для суммы")
#         # вызов функции на ответ пользователя
#         bot.register_next_step_handler(message, summa)
#     elif message.text == "разность":
#         pass

bot.infinity_polling()




# Прикрутить телеграмм бота к задачам с предыдущего семинара:
# Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)
# Подумайте как наделить бота ""интеллектом"" (есть алгоритм, позволяющий выяснить какое количесвто конфет необходимо брать, 
# чтобы гарантированно победить, соответственно внедрить этот алгоритм боту )



#Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP
# Прикрутить бота к задачам с предыдущего семинара:
# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования
# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.