""" 
1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет """
day=int(input('Введите день недели '))
if day==6 or day==7 :
    print("выходной")
else:
    print("не выходной")

""" 
1.Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
"""

for i in (0,1):
    x=bool(i)
    for j in (0,1):
        y=bool(j)
        for k in (0,1):
            z=bool(k)
            if ~(x and y and z) == (~x and ~y and ~z):
                result=True
            else:
                result=False
            print("¬({0} ⋁ {1} ⋁ {2}) = ¬{0} ⋀ ¬{1} ⋀ ¬{2}  {3}".format(i,j,k,result))


"""
2.Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3 """

print("\n""Принимает точку (X и Y) и выдаёт номер четверти плоскости")
x=int(input('Введите X '))
y=int(input('Введите Y '))
if x>0 and y!=0 :
    if y<0 :
        print("№ 4")
    else:
        print("№ 1")
if x<0 and y!=0:
    if y<0 :
        print("№ 3")
    else:
        print("№ 2")
if x==0 or y==0 :
    if y==0 :
        print("Точка на оси X")
    else:
        print("Точка на оси Y")

""" 
1.Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)."""

part=int(input("\n"'Введите номер четверти '))
if part==1:
    print("x > 0 и y > 0")
elif part==2:
    print("x < 0 и y > 0")
elif part==3:
    print("x < 0 и y < 0")
elif part==4:
    print("x > 0 и y < 0")
else:
    print("такой четверти несууществует")


"""
2.Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21 """

print("\n""расстояние между точками в 2D пространстве.")
a=input('координаты точки А ')
b=input('координаты точки В ')

list_num1=a.split(",")
list_num2=b.split(",")
AC = (int(list_num2[0])-int(list_num1[0]))
BC = (int(list_num2[1])-int(list_num1[1]))

length=((AC**2)+(BC**2))**(0.5) # корень
print(int(length * 100) / 100)

