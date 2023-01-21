def view_result(a):
    print(f'Результат: {a}')

def get_operate(num):
    if num:
        return input("выбор действия (+,-,*,/,//,%) ")
    else :
        return input("выбор действия (+,-,*,/) ")

def get_type():
    return int(input("введите 1 для целых, 0 для комплексных "))

def get_value(select):
    if select==1:
        return int(input('int value = '))
    else:
        return complex(input('complex value = '))