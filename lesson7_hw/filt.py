def set_filter():
    select=input("выполнить сортировку? Y / N: ").lower()
    if select =="y".lower():
         return int(input("1 по имени , 0 по id "))
    else :
        print("сортировка не выполняется")
        return -1

def sortByinex(inputStr,num):
        temp=inputStr.split(",")
        print(temp[num])
        return temp[num] 

    
def sort_contacts(pos):   
    somefile = open("lesson7_hw\\database.txt", "r",encoding='utf-8')
    result=sorted(tuple(somefile),key=lambda cont: sortByinex(cont,pos))
    somefile.close()
    
    newdata = open("lesson7_hw\\database.txt", "w",encoding='utf-8')
    for s in result:
        newdata.write(s)
    newdata.close()