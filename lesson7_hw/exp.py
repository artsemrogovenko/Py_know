def init_operate():
    return int(input("0 для просмотра, 1 для добавления "))

def view_base():
    somefile = open("lesson7_hw\\database.txt", "r",encoding='utf-8')
    for s in somefile:
        out=s.split(',')
        print(*out,end="")
    somefile.close()

def name_lastname():
    somefile = open("lesson7_hw\\database.txt", "r",encoding='utf-8')
    for s in somefile:
        out=s.split(',')
        print(*out[1:3])
    somefile.close()