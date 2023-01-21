import view
import module


def calc ():
    type_num = view.get_type()
    a = view.get_value(type_num)
    b = view.get_value(type_num)
    op = view.get_operate(type_num)
    module.init(a,b)
    if op in ['+','-','*','/','//','%']:
        if op == '+':
            view.view_result(module.sum())
        elif op == '-':
            view.view_result(module.dif())
        elif op == '*':
            view.view_result(module.mult())
        elif op == '/':
            view.view_result(module.div())
        elif op == '//':
            if type_num == 1:
                view.view_result(module.div_int())
            else:  print('недоступная операция для комплексных чисел!')
        elif op == '%':
            if type_num == 1:
                view.view_result(module.div_ost())
            else:  print('недоступная операция для комплексных чисел!')
    else: print("ошибка ввода действия")