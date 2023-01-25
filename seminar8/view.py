def view_students(journal):
    for i in journal:
        print(i)


def student_marks(journal, student):
    for j in journal[student]:
        print(f"{j} {journal[student][j]}")
