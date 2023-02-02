import telebot
from telebot import types


bot = telebot.TeleBot("")
mode=False
result="0"


""" Прикрутить бота к задачам с предыдущего семинара:
Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования(отдельный файл с полями - имя, время,сообщение) """

kb = types.InlineKeyboardButton
keyboard = types.InlineKeyboardMarkup(row_width=4)  # создание клавиатуры
keyboard.add(kb("%", callback_data="%"), kb("<<", callback_data="<<"),
             kb("C", callback_data="C"), kb("/", callback_data="/"))
keyboard.add(kb("7", callback_data="7"), kb("8", callback_data="8"),
             kb("9", callback_data="9"), kb("*", callback_data="*"))
keyboard.add(kb("4", callback_data="4"), kb("5", callback_data="5"),
             kb("6", callback_data="6"), kb("-", callback_data="-"))
keyboard.add(kb("1", callback_data="1"), kb("2", callback_data="2"),
             kb("3", callback_data="3"), kb("+", callback_data="+"))
keyboard.add(kb("0", callback_data="0"), kb(".", callback_data="."),
             kb("j", callback_data="j"), kb("=", callback_data="="))
keyboard.add(kb("(", callback_data="("), kb(")", callback_data=")"))

@bot.message_handler(commands = ['start'])#
def welcome_to_calc(message):
    global result
    import time
    result="0"
    tgbot_log = open("lesson10_hw\.venv\log.txt", 'a')
    print(f"{message.from_user.first_name},{time.ctime()},{message.text}",file=tgbot_log)
    tgbot_log.close()
    bot.send_message(message.chat.id,result, reply_markup=keyboard)

calculation=0
list_buttons=['(',')','j','.','%','/','*','+','-',"0","1","2","3","4","5","6","7","8","9"]
@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global result
    import time
    global calculation
    mode = 0
    data = query.data
    tgbot_log = open("lesson10_hw\.venv\log.txt", 'a')
    print(f"{query.message.chat.first_name},{time.ctime()},{data}", file=tgbot_log)
    tgbot_log.close()
    if data == 'j':
        mode = 1
    elif data == "<<" and result != "0":
        if result[len(result)-1]=='j':
            mode=0
        result = result[:-1]
    elif data == "C":
        mode=0
        result = "0"

    if calculation==1:
        result=data
        calculation=0

    elif data == "=": 
        
        calculation=1
        try:            
            if mode == True:
                result = str(complex(result))                  
            else:
                result = str(eval(result))
        except: 
            result="Ошибка"  
       # print(query.message.first_name.f,time.ctime(),result)
    elif data in list_buttons:
            if result=="0":
                result=data
            else:
                result += f"{data}"

    if result=="Ошибка": 
        result="0"
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.id,text=result,reply_markup=keyboard)
    

bot.infinity_polling()
