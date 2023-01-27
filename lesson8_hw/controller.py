import create
import view
import read
import write
import csv
# book={}
# sciences=[]

book = {'Rik Pruppers': {'Химия': [1,2,3],'Черчение': [4,5,5]}, 
        'Ton Goralczyk': {'Физика': [4,5,4],'Черчение': [4,5,1]}, 
        'Simon Pruppers': {'Информатика': [4,4,4],'Физика': [4,5,4]},
        'Nathan Morgenstern': {'Черчение': [4,5,1],'Физика': [4,5,5]}}
sciences=['Черчение', 'Химия', 'Физика', 'Информатика']


loop=True

def start():
 while loop:    
     try:   
            print("предметы ",sciences)
            op=int(input("\
        1 Добавление нового студента (Поля - имя, фамилия)\n\
        2 Добавление предмета\n\
        3 Добавление оценки ученику по предмету\n\
        4 Показ списка учеников\n\
        5 Показ листа оценок конкретного ученика\n\
        6.Генерация сотни участников и занесение журнал\n\
        7.Вывод средней оценки ученика по одному предмету\n\
        8.Вывод среднего балла по школе по конкретному предмету\n\
        9.Вывод количества учеников претендующих на золотую медаль (все оценки либо 4 либо 5)\n\
        0 Выход из программы\n"))
            if op == 1:
                create.add_student(book)
            elif op == 2:
                subject=input("имя предмета ")
                if create.add_theme(sciences,subject)==True:
                    sciences.append(subject)
                else:  print("такой предмет уже есть")
            elif op == 3:
                name=input("имя ученика ")
                subject=input("имя предмета ")
                grade=int(input("добавить оценку "))
                create.set_mark(book,name,subject,grade,sciences)
            elif op == 4:
                view.view_students(book)
            elif op == 5:
                name=input("имя ученика ")
                view.student_marks(book,name)
            elif op == 6:
                n=read.read_file_words('names')
                s=read.read_file_words('surnames')
                sbj=read.read_file_words('subjects')
                for i in sbj:
                 if create.add_theme(sciences,i)==True:
                    sciences.append(i)
                create.random_people(book,n,s,sciences)
            elif op==7:
                name=input("имя ученика ")
                subject=input("имя предмета ")
                print("средний балл",view.student_progress_subj(book,name,subject))
            elif op==8:
                subject=input("имя предмета ")
                print("средний балл по школе",view.school_average(book,subject))
            elif op == 9:
                 print(view.student_medal(book))
            elif op == 0:
                exit()
            # export=input("записать изменения в файл? Y/N ").lower()
            # if export=='y':
            #    write.csv_export(book,sciences)
     except Exception :
             print("ошибка")
 start()
