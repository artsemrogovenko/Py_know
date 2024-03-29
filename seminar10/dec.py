import telebot
from telebot import types

bot = telebot.TeleBot()

def decorator(func):
    import time
    def wrapper(*args,**kwargs):
        print("its ur programm")
        start = time.time()
        response = func(*args,**kwargs)
        end = time.time()
        print(f"ваша функция работает за {end - start} секунд")
        return response
    return wrapper

@decorator
def request_url(url):
    import requests
    response = requests.get(url)
    return response

request_url("https://ya.ru")

@bot.message_handler(commands=['start']) # вызов функции по команде в списке
def start(message):
    pass