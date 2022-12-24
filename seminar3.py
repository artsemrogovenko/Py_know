#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# n = input()
# summ = 0
# for i in n:
#     if i.isdigit(): # если элемент число
#         summ+=int(i)
# print(summ)

# n = float(input())
# len_num = len(str(n))-1
# summ=0
# while n!=int(n):
#     n= round(n*10,len_num)
#     print(n)
# while n>0:
#     summ+=n%10
#     n = n//10
# print(summ)

#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# n = int(input())
# #пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# fact_list = []
# factorial = 1
# for i in range(1,n+1):
#     factorial*=i
#     fact_list.append(factorial)
# print(fact_list)

# n = int(input())
# dict_num = {}
# for i in range(1,n+1):
#     dict_num[i] = round((1+1/i)**i,2)
# print(dict_num)
# print(sum(dict_num.values()))

# import random
#
# n = int(input())
# list_num = [random.randint(-n,n) for i in range(n)]
# print(list_num)

# file = open("File.txt","r")
# multi = 1
# list_str = file.readlines()
# print(list_str)
# list_num = list(map(str.strip,list_str))
# print(list_num)
# list_num = list(map(int,list_num))
# print(list_num)
# for i in file:
#     multi*=list_num[int(i)]
# print(multi)

# import datetime
# def random_int(num):
#     rand = datetime.datetime.now().microsecond/10**6
#     return int(num*rand)

# a = [1,2,3,4,5,6]
# print(a)
# random_int(5)
# for i in range(len(a)-1,-1,-1):
#     j = random_int(i+1)
#     a[i],a[j] = a[j],a[i]
# print(a)

"""19. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел. 
n вводит пользователь вывести рандомное число в диапазоне от 0 до n
 """
import datetime
def random_int(num):
    rand = datetime.datetime.now().microsecond / 10**6
    return int((num + 1) * rand)

""" 20. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число. """

my_list = ['12',23,"qwer",23.4]
print(my_list)
x=float(input("есть ли число и покажет индекс "))
for i in range(len(my_list)):
    if my_list[i]==x:
        print("индекс",i)
        break
else:
    print("совпадений нет")

""" 21. Напишите программу, которая определит позицию второго вхождения строки в 
    списке либо сообщит, что её нет.
*Пример:*

- список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
- список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
- список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
- список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
- список: [], ищем: "123", ответ: -1  """
print("определит позицию второго вхождения искомого в "
        "списке либо сообщит, что её нет")
string = ["123", "234", 123, "567"]
substring = "123"
count = 0
print(string)
print("искомое",substring,type(substring))
for i in range(len(string)):
    if string[i] == substring:
        count += 1
    if count == 2:
        print("ответ ",i)
        break
else:
    print("ответ -1")


# #Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# a = ["sr","ere","12","wewe"]
# n = int(input())
# for i in a:
#     if i.isdigit() and int(i) == n:
#         print(a.index(i))
# n = int(input())
# if n in a:
#     print(a.index(n))
# else:
#     print(-1)

#Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
# import datetime
# import time
# # def random_int(num):
# #     rand = datetime.datetime.now().microsecond%num
# #     return rand+1
#
# for i in range(10):
#     time.sleep(0.01)
#     print(datetime.datetime.now().microsecond)

# list_str = ["йцу", "фыв", "ячс", "цук", "йцукен"]
# sub_str = "йцу"
# count=0
# for i in range(len(list_str)):
#     if list_str[i] == sub_str:
#         count += 1
#     if count == 2:
#         print(i)
#         break
# else:
#     print(-1)
