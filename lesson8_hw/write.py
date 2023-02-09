import csv

def csv_export(journal,subjects):
    with  open("lesson8_hw/users.csv", "w",encoding="utf-8", newline='') as csvfile:
        titles = ['Ученик']
        for item in subjects:
            titles.append(item)        
        csv.writer(csvfile, delimiter=";").writerow(titles)
        for student in journal:            
            out=[";" for i in range(len(titles))]
            data=f"{student}"
            for obj in journal[student]: 
                index=titles.index(obj) 
                for title in titles:
                    if obj==title:
                        out[index]=','.join(map(str, journal[student][obj]))+";"
            data+=''.join(map(str, out))
            csvfile.write(f"{data}\n")
        csvfile.close()
