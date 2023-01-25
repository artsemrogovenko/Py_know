def add_student(journal):
    temp = 0
    name = input("Введите имя фамилию студента ")
    for key in journal.keys():
        if name == key:
            temp = 1
            print("такой ученик уже есть")
    if temp == 0:
        journal[name] = {}


def add_theme(sciences, new_subject):
    iteration = 0
    for j in sciences:
        if j == new_subject:
            iteration = 1
            print("такой предмет уже есть")
            return False
    if iteration == 0:
       return True


def set_mark(journal, student, subject, mark, sciences):
    for j in sciences:
        if j not in journal[student]:
            journal[student][j] = []
    journal[student][subject].append(mark)
