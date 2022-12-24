""" 27. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел. """
def get_min_max(list_int):
    min_num = list_int[0]
    max_num = list_int[0]
    for i in range(1, len(list_int)):
        item = list_int[i]
        if max_num < item:
            max_num = item
        if min_num > item:
            min_num = item
    return max_num, min_num

in_string=input("введите числа через пробел ").split()
print(in_string)
num=list(map(int,in_string))
print("max = ",max(num),"min = ",min(num))
""" 28. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
1) с помощью математических формул нахождения корней квадратного уравнения
2) с помощью дополнительных библиотек Python """
import math
a = int(input('Введите коэф. a '))
b = int(input('Введите коэф. b '))
c = int(input('Введите коэф. c '))
# d = (b ** 2) - 4 * a * c
# if d < 0:
#     print ('Корней нет!')
# if d == 0:
#     print('x =', -(b) / (2 * a))
# if d > 0:
#     print('x1 =', (-b + d ** 0.5) / (2 * a))
#     print('x1 =', (-b - (d ** 0.5)) / (2 * a))

d = math.pow(b, 2) - 4 * a * c
if d < 0:
    print ('Корней нет!')
if d == 0:
    print('x =', -(b) / (2 * a))
if d > 0:
    print('x1 =', (-b + math.sqrt(d)) / (2 * a))
    print('x1 =', (-b - math.sqrt(d) / (2 * a)))


""" 29. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел. """
print("(наименьшее общее кратное) двух чисел")
a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
max_num = max(a, b)
for i in range(max_num, a * b + 1, max_num):
    if i % a == i % b == 0:
        print(i)
        break

#Задайте строку из набора чисел.
#Напишите программу, которая покажет большее и меньшее число.
#В качестве символа-разделителя используйте пробел.
# a = input()
# list_num = a.split()
# list_num = list(map(int,list_num))
# print(max(list_num),min(list_num))

#Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами
# import math
#
# a = int(input())
# b = int(input())
# c = int(input())
#
# d = b**2 - 4*a*c
# if a!=0:
#     if d>0:
#         x1 = (-b + math.sqrt(d))/(2*a)
#         x2 = (-b - math.sqrt(d))/(2*a)
#         print(x1,x2)
#     elif d == 0:
#         x = -b / (2 * a)
#         print(x)
#     else:
#         print("net korney")
# else:
#     x = -c/b
#     print(x)
