import csv

def csv_export(journal,subjects):
 with  open("lesson8_hw/users.csv", "w", encoding="cp1251", newline='') as csvfile:
        titles = ['Ученик']
        for item in subjects:
            titles.append(item)
        writer = csv.writer(csvfile,  delimiter=";")
        for student in journal:            
            out=[";" for i in range(len(titles))]
            data=f"{student}"
            for obj in journal[student]: 
                index=titles.index(obj) 
                temp=""
                for title in titles:
                    if obj==title:
                        area = journal[student][obj]
                        for value in str(area):
                            if value.isdigit():
                                temp+=f"{value},"                        
                        out[index]=temp[:len(temp)-1]       
            data+=f"{out}"           
            csv.writer(csvfile,delimiter=" ").writerow(data)
        csvfile.close()
