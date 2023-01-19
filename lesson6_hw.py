# С помощью использования лямбд, filter, map, zip, enumerate, list comprehension
""" **44. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
Пример:
A (3,6); B (2,1) -> 5,09
A (7,-5); B (1,-1) -> 7,21 """
import random
import math
print("координаты точки через запятую")
e = [input(f"точка {i+1}= ") for i in range(2)]
e = list(map(lambda x: x.split(","), e))

AC = (int(e[0][0])-int(e[1][0]))
BC = (int(e[0][1])-int(e[1][1]))
print(math.sqrt(((AC**2)+(BC**2))))

""" 45. Найти сумму чисел списка стоящих на нечетной позиции """
print("сумма чисел списка стоящих на нечетной позиции ")
a = [random.randint(2, 50) for i in range(7)]
print(a)
sum_pos = 0
pos = list(filter(lambda x: True if a.index(x) % 2 == 1 else False, a))
print(pos)
for x in pos:
    sum_pos += x
print("сумма = ", sum_pos)

""" 46. Найти произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд) """
import random
n = int(input("произведение пар чисел\nколичество чисел "))
pairs = [random.randint(2, 10) for i in range(n)]
print(pairs)
multiply = lambda x,y: x*y[(len(y)-1)-y.index(x)]
result= [multiply(pairs[i],pairs) for i in range(len(pairs)//2)]
if len(pairs)%2==1:
    result.append(pairs[(len(pairs)//2)]**2) # умножу среднее значение на самого себя
print(result)

""" 47.Сформировать список из N членов последовательности
Для N=5: 1,-3,9,-27,81 (каждый член больше предыдущего в три раза, знак чередуется) """

n_size = int(input("список из N, размерность "))
result = [3**i for i in range(n_size)]
print(result)
result = list(map(lambda x: x*-1 if result.index(x) % 2 == 1 else x*1, result))
print(result)
