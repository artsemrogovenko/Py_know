def view_students(journal):
    for i in journal:
        print(i)


def student_marks(journal, student):
    for j in journal[student]:
        print(f"{j} {journal[student][j]}")


def student_progress_subj(journal,student,subj):
        count=0
        summ=0
        for nums in journal[student][subj]:
            summ+=nums
            count+=1
        return summ/count

def school_average(journal,subj):
    count=0
    AverageOfGrades=0
    for student in journal:
       for key in journal[student].keys():
        if subj == key:
            count+=1
            AverageOfGrades+=student_progress_subj(journal,student,subj)
    return AverageOfGrades/count

def student_medal(journal):
    count_medal_obj=0
    count_good_mark=0
    obj_count=0
    student_count=0
    compare_grade=[]
    for student in journal:
        for obj in journal[student]:
            obj_count+=1
            for grades in journal[student][obj]:
                compare_grade.append(grades)
            for num in compare_grade:
                if num not in [4,5]:
                    break
                else:
                    count_good_mark+=1  
                    # если количество хороших оценок совпало 
                    # с количеством оценок в предмете
            if count_good_mark == len(journal[student][obj]): 
                count_medal_obj+=1                      
            compare_grade=[]
            count_good_mark=0
            # если количество предметов с хорошей успеваемостью совпало 
            # с количеством предметов ученика
        if count_medal_obj ==  len(journal[student]):
            student_count+=1 
            print(student)
        obj_count=0  
        count_medal_obj=0    
    return student_count