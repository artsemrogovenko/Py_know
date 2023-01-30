#скачиваем библиотеку pip install pytelegrambotapi
# python -m имяОкружения .папкаОкружения
import telebot
from telebot import types
# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

info="Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.\
За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход."

get_sweets = 0
sweets= 221
bot = telebot.TeleBot()
player_name=""
player_list=["",""]

@bot.message_handler(commands = ['start'])#вызов функции по команде в списке
def welcome_sweet_game(message):
    bot.send_message(message.chat.id,f"{info}") #отправка сообщения (кому отправляем, что отправляем(str))
    select_mode(message)


def select_mode(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)  # создание клавиатуры
    but1 = types.KeyboardButton("игра c человеком")  # создание кнопок
    but2 = types.KeyboardButton("игра с ботом")
    but3 = types.KeyboardButton("игра с умным ботом")
    markup.add(but1)  # добавление кнопок
    markup.add(but2)  # добавление кнопок
    markup.add(but3)  # добавление кнопок
    bot.send_message(message.chat.id, "Выбери вариант ниже", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def controller(message):
    global player_list
    global sweets
    global player_name
    if message.text=="игра c человеком":    
        sweets = 221     
        bot.send_message(message.chat.id,f"Ввести имена игроков через пробел")
        bot.register_next_step_handler(message,input_names)            
    if message.text=="игра с ботом":
        sweets = 221
        player_list[0]=message.from_user.first_name
        player_list[1]="bot"
        player_name=player_list[0]
        bot_think(message)
    if message.text=="игра с умным ботом":
        sweets = 221
        player_list[0]=message.from_user.first_name
        player_list[1]="smart_bot"
        player_name=player_list[0]
        smart_bot(message)
    else:
        select_mode(message)


def input_names(message):
    global player_list
    global player_name 
    player_list=str(message.text).split()
    player_name=player_list[0]
    start(message)
    

def start(message):
    global sweets
    bot.send_message(message.chat.id,f"ходит {player_name}")
    if sweets>=28:
        bot.send_message(message.chat.id,f"Введите количество не больше 28")#отправка сообщения (кому отправляем, что отправляем(str))
    else:
        bot.send_message(message.chat.id,f"Введите количество")
    bot.register_next_step_handler(message,user_input)


def user_input(message):
    global get_sweets 
    try:   
        get_sweets = int(message.text)
        check_count(message)
    except: 
        # img =  open("lesson9_hw\.tgbot\sticker.webp","rb")
        # bot.send_photo(message.chat.id, img)
        # img.close
        bot.send_message(message.chat.id,f"ошибка ввода")
        start(message)
    


def check_count(message):
    if 29>get_sweets>=1 and sweets-get_sweets>=0:  #если не превышено количество забираемых
        set_count(message)
    else:
        bot.send_message(message.chat.id,"такое количество нельзя взять")
        bot.register_next_step_handler(message,user_input)



def set_count(message):
    global sweets
    global player_name
    sweets=sweets-get_sweets
    bot.send_message(message.chat.id,f"осталось {sweets}")
    if sweets==0:
       bot.send_message(message.chat.id,f"победил {player_name}")
       welcome_sweet_game(message)
    else:
        if player_name == player_list[0]:
            player_name = player_list[1]
        else:
            player_name = player_list[0]

        if player_name == "smart_bot":
            smart_bot(message)
        elif player_name == "bot":
            bot_think(message)
        else:
            start(message)


def bot_think(message):
    import random
    global get_sweets
    global player_name
    player_name = "bot"
    if sweets > 28:
        get_sweets = random.randint(1, 29)
    elif sweets<28:
        get_sweets = random.randint(1, sweets)
    format_mes_bot(message)


def smart_bot(message):
    global get_sweets
    global player_name
    player_name="smart_bot"
    if sweets==221:
        get_sweets=sweets-((sweets//29)*29)
    else:
        get_sweets=29-get_sweets
    if sweets<=28:
        get_sweets=sweets
    format_mes_bot(message)

def format_mes_bot(message):
    if get_sweets in [1,21]:
        ending='у'
    elif get_sweets in [2,3,4,22,23,24]:
        ending='ы'
    else:
        ending=''
    bot.send_message(message.chat.id, f"{player_name} забирает {get_sweets} конфет{ending}")
    check_count(message)


bot.infinity_polling()


# Прикрутить телеграмм бота к задачам с предыдущего семинара:
# Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)
# Подумайте как наделить бота ""интеллектом"" (есть алгоритм, позволяющий выяснить какое количесвто конфет необходимо брать, 
# чтобы гарантированно победить, соответственно внедрить этот алгоритм боту )
