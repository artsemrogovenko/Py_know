"""30 Вычислить число c заданной точностью d
Пример:
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
 """

import math
num=math.pi
acc=input("Введите точность отображения ")
temp=float(acc)
print(num)
if math.pow(10,-1)>=temp>=math.pow(10,-10):
    acc=acc.split(".")
    len_str=int(len(acc[1]))
    print(f"вывод {len_str} знака после запятой")
    parameter=f".{len_str}f" #преобразование в строку для агрумента форматирования
    len_str=len(acc[1])
    print(f"{num:{parameter}}")
else:
    print("недопустимое значение")

""" 
31 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N. """
print("\nсписок множителей числа")
n = int(input("натуральное число "))
divisor = 2
string_divisors = []
while n != 1:
    if n//divisor != n/divisor:
        divisor += 1
    else:
        n /= divisor
        string_divisors.append(divisor)
        divisor = 2
        continue
print(string_divisors)

""" 32 Задайте последовательность чисел. Напишите программу, 
которая выведет список неповторяющихся элементов исходной последовательности. """

pi = str(math.pi).split(".")
digits = pi[1]  # числа после точки от числа пи
serial_nums = []  # список ждя последовательности чисел
non_repeat = []  # для неповторяющихся элементов
count = 0
for digit in digits:  # заполняю
    serial_nums.append(digit)
print("последовательность чисел\n", serial_nums)
for element in serial_nums:
    for i in range(len(serial_nums)):
        if serial_nums[i] == element:
            count += 1
            index = i
        elif count > 1:
            count = 0
            break
    if count == 1:
     non_repeat.append(serial_nums[index])
print(non_repeat, "не повторяются")

""" 33 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
и записать в файл многочлен степени k.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0  """

print("\nсписок коэффициентов")
import random
k=int(input("Ввести степень "))
polynomial=""
count=k*1
while count>0:
    generated=random.randint(0,100)
    if generated!=0 and generated!=1:
        polynomial+=f"{generated}*x**{count} "
        count-=1
    else:
        polynomial+=f"x**{count} "    
    if count>=1:
          polynomial+=("+ ")
polynomial+=f"+ {random.randint(0,100)}"
print(polynomial)
output=open("lesson4_hw\polynomial.txt","a",encoding='utf-8')
output.write(f"степень={k} {polynomial}\n")
output.close()

""" 35 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов. """
print("\ncумма по двум многочленам")
file_first=open("lesson4_hw\prim.txt","r")
file_second=open("lesson4_hw\sec.txt","r")
# print(file_first.read(), end="  +  ")
# print(file_second.read())
list_monomial=file_first.readline().split("+")+file_second.readline().split("+")
file_first.close()
file_second.close()

ratio_list=[] #  список для коэфициентов
variable_list=[] # список для переменных
monomial = {}   # неповторяющийся список переменных

summ_s = 0 # для лжиночных коэф
for element in list_monomial: 
    count_a = 0
    result = ""
    koef=""
    sum_digit = 0
    count_digit = 0
    buffer=0
    for i in element:

      if i.isalpha() or count_a ==1:
        result += i
        count_a = 1

      if (i.isdigit() and count_a==0) and element!=i :
          koef+=i
          count_digit = 1
    if element.isdigit()==False and count_digit==0: # если элемент из букв и нет коэф
        koef=1  
    if element.isdigit(): # если элемент полностью число
        summ_s += int(element)

    if element.isdigit()==False : # если элемент состоит из букв и есть коэфициент но не просто число
      monomial[result]=list_monomial.index(element)
    ratio_list.append(koef)
    variable_list.append(result)

# print("сумма одиночн ",summ_s)
str_out=""
for key in monomial.keys():
    sum_koef=0    
    for sub_str in variable_list:
        if sub_str==key :
            sum_koef=sum_koef+int(ratio_list[variable_list.index(sub_str)]) # прибаляю коэфициент
    if sum_koef>1:
        str_out+=f"{sum_koef}{key} +"
    else: # если у переменной коэф нет или он единица
        str_out+=f"{key} +"

sum_files=open("lesson4_hw\summ.txt","w")

if summ_s != 0:     
 print(str_out,summ_s)
 print(str_out,summ_s,file=sum_files)
else:
 str_out=str_out[:-1]
 print(str_out)
 print(str_out,file=sum_files)

sum_files.close()