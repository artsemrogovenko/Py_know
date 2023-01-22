import exp
import imp
import filt

def start():
    print("телефонный справочник")
    try: 
        edit = exp.init_operate() 
        if edit == 1:
            contact = imp.get_contact()
            imp.write_file(contact)
        elif edit == 0:
            select = int(input("1 показать всю базу, 0 только имена и фамилию "))
            if select:
                exp.view_base()
            else:
                exp.name_lastname()
    except Exception :
        print("неверное действие")
        
    sorting = filt.set_filter()

    if sorting in [0, 1]:        
        filt.sort_contacts(sorting)

    retry=input("Провести еще операцю? Y/N ").lower()
    if retry=='y':
            start()
    else: 
            exit()