def get_contact():
    return input("введите значения через запятую\n(id,имя,фамилию,телефон,комментрий)\n")


def write_file(input_data):
    with open("lesson7_hw\\database.txt", "a",encoding='utf-8') as somefile:
     somefile.write(input_data+'\n')
     somefile.close()
