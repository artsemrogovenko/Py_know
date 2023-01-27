
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
            return False
    if iteration == 0:
       return True


def set_mark(journal, student, subject, mark, sciences):
    for j in sciences:
        if j not in journal[student]:
            journal[student][j] = []
    journal[student][subject].append(mark)

import random

def random_people(journal,names,surnames,subjects):
    old_list=len(journal)
    while len(journal) < old_list+100:
        temp=0
        n=random.choice(names)
        s=random.choice(surnames)
        sbj=random.choice(subjects)
        generated=f"{n} {s}"
        for key in journal.keys():
            if generated == key:
                temp = 1
        if temp == 0:
            journal[generated]={}
            journal[generated][sbj]=[]
            for _ in range(5):
                journal[generated][sbj].append(random.randint(1,5))