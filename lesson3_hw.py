""" 22.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12 """
print("сумма элементов на нечётной позиции")
list_num=[2, 3, 5, 9, 3]
summ=0
print(list_num)
for i in range(1,len(list_num),2):
    summ+=list_num[i]
    print(list_num[i], end =" ") 
print("ответ:",summ)

""" 23. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15] """
print("\nпроизведение пар чисел списка.\nпервый и последний элемент, второй и предпоследний и т.д.")
numbers = [2, 3, 4, 5, 6]
print(numbers)
multi_pair = []
backstep = 0
stopindex = (len(numbers)//2)
for i in numbers:
    if numbers.index(i) == stopindex:
        break
    print(i, "*", numbers[len(numbers)-backstep-1])
    multi_pair.append(i * numbers[len(numbers)-backstep-1])
    backstep += 1
if len(numbers) % 2 > 0:  # если элементов нечетное количество
   print("{value} * {value}".format(value=numbers[stopindex]))
   multi_pair.append(numbers[stopindex]**2)
print("multi_pair =", multi_pair)

""" 24.Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19 """
print("разница между максимальным и минимальным значением дробной части")
number = [1, 4.01, 11, 5, 10.2]
max_num = 0
temp = [""]
for i in number:
  if int(i) != i:  # если элемент с точкой. нахожу макс число
    if max_num < i:
        max_num = i
min_num = max_num
for j in number:
  if int(j) != j:  # если элемент с точкой. нахожу мин число
    if j < min_num:
        min_num = j
print(min_num, max_num)
min_num += int(max_num)-int(min_num)  # привожу к общему знаменателю
# и вывожу разницу  abs для вывода положительного числа
print("ответ= ", "{:.2f}".format(abs(max_num-min_num)))


""" 25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10 """
print("преобразование десятичного числа в двоичное ")
number=int(input("введите число "))
result=number
binary=[]
while (result//2) >= 1: 
    binary.insert(0,result%2)
    result//=2
if result == 1:
     binary.insert(0,result%2)
print(binary) 


""" 26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] """

k = int(input("количество чисел Фибоначчи c отриц числами "))
fib = []
for a in range((k*2)+1):  # задаю размерность массива и заполняю нулями
    fib.append(0)
middle = len(fib)//2  # средний индекс с нулем
if k > 0:
  fib[middle+1] = 1
  fib[middle-1] = 1
for i in range(1, middle):
    fib[middle+i+1] = fib[middle+i]+fib[middle+i-1]
    if (middle+i+1) % 2 == 0:  # если индексы левее от середины делятся без остатка, пишу инвертированное число из правой части
      fib[middle-i-1] = fib[middle+i+1]*-1
    else:
      fib[middle-i-1] = fib[middle+i+1]  # если нет, то копирую положительное

if k % 2 != 0:  # для правильного отображения нечетного количества чисел
   e = 0
   while e < (len(fib)//2)-1:
    fib[e] = fib[e]*-1
    e += 1
print(fib)
