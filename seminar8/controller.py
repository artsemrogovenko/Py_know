import create
import view
book={}
sciences=[]
loop=True

def start():
 while loop:    
    try:   
            op=int(input("\
        1 Добавление нового студента (Поля - имя, фамилия)\n\
        2 Добавление предмета\n\
        3 Добавление оценки ученику по предмету\n\
        4 Показ списка учеников\n\
        5 Показ листа оценок конкретного ученика\n\
        0 Выход из программы\n"))
            if op == 1:
                create.add_student(book)
            elif op == 2:
                subject=input("имя предмета ")
                if create.add_theme(sciences,subject)==True:
                    sciences.append(subject)
            elif op == 3:
                name=input("имя ученика ")
                subject=input("имя предмета ")
                grade=int(input("добавить оценку "))
                create.set_grade(book,name,subject,grade,sciences)
            elif op == 4:
                view.view_book(book)
            elif op == 5:
                name=input("имя ученика ")
                view.student_marks(book,name)
            elif op == 0:
                exit()
            print(book)
            print("предметы ",sciences)
    except Exception :
            print("ошибка")
 start()
