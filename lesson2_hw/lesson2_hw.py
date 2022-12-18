""" 14 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11 """
number=input("введите число ")
exclude=-1
summ=0
for index in range(len(number)):
     if number[index]=="." or number[index]==",": # от текущего индекса с шагом длинны искомого текста
        exclude=index
for element in range(len(number)):
    if element!=exclude:
        summ+=int(number[element])
print("сумма чисел = ",summ)


""" 15 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)"""
number=int(input("набор произведений чисел от 1 до "))
result=1
string="1"
list_result=[]
list_result.insert(0,string)
for i in range(number):
    result*=(i+1)
    if i<number-1:
        print(result, end =",")     
    if i > 0 :
        string+='*'+str(i+1)  
        list_result.insert(i,string)     
print(result,list_result,"\n")

""" 16 Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
Пример:
- Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
        Сумма 9.06 """
cycles=int(input("список из n чисел последовательности (1 + 1/n)^n "))
sum2=0;
for i in range(1,cycles+1):
    sum2+=(1 + 1/i)**i
print("суммма",int(sum2*100)/100,"\n")

""" 17 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
Позиции хранятся в файле file.txt в одной строке одно число."""
import random
n=int(input("список из N в промежутке [-N, N] "))
generated=[]
result=1
data=open("lesson2_hw/file.txt","r")
for i in range(5):
    generated.insert(i,random.randint(n*(-1), n))
    while generated[i]==0:
        generated.insert(i,random.randint(n*(-1), n))
print(generated)
for line in data:
    result*=generated[int(line)]
    print("result = ",result)
data.close()    
print("произведение = ",result,"\n")

""" 18 Реализуйте алгоритм перемешивания списка. """


def mixer(arr, verse):
    mixed = []
    for _ in range(len(arr)):
        mixed.append("")
    index = 0
    if verse == True:
        mixed[len(text)-1] = text[len(text)-2]
    elif verse == False:
        mixed[len(text)-1] = text[len(text)-1]
    for i in range(0, len(text)-1, 2):
        if i < len(arr):
            mixed[index] = arr[i+1]
            index += 1
    for j in range(1, len(arr)-1, 2):
        if i < len(arr):
            mixed[index] = arr[j-1]
            index += 1
    return mixed


text = list("поверяющий")
res = []
print(text)
if len(text) % 2 == 0:
    res = mixer(text, True)
else:
    res = mixer(text, False)
print(res)


