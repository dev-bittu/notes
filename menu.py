from pickle import dump, load

FILE = open('student_data.dat', 'ab+')

def exit_program():
    FILE.close()
    exit()

def add_record():
    student_name = input('Enter Student Name: ')
    contact_no = input("Enter student's contact number: ")
    record = {
        student_name: contact_no
    } 
    dump(record, FILE)

def search_record():
    name = input('\nEnter name to be searched: ')
    found = False
    try:
        while not found:
            data = load(FILE)
            if name in data.keys():
                found = True
    except:
        pass
    finally:
        if found:
            print('\nData exists\n')
        else:
            print('\nData doesn\'t exists')

def modify_record():
    modify = input('What you want to modify (student_name or contaxct_no) [S/C]: ').lower()
    try:
        data = []
        while True:
            d = load(FILE)
            data.append(d)
    except:
        pass
    if modify == 's':
        name = input('Enter old name (to be modified): ')
        new_name = input('Enter new name for the student: ')
        for d in data:
            if name in d.keys():
                data.remove(d)
                for i, j in d.items():
                    data.append(
                        {
                            new_name: j
                        }
                    )
                break
        else:
            print(f'Student of name "{name}" doesn\'t exists')

    elif modify == 'c':
        contact_no = input('Enter old contact no (to be modified): ')
        new_contact_no = input('Enter new contact no for the student: ')
        for d in data:
            if contact_no in d.values():
                name = list(d.keys())[0]
                print(name)
                data.remove(d)
                for i, j in d.items():
                    data.append(
                        {
                            name: new_contact_no
                        }
                    )
                break
        else:
            print(f'Student of contact number "{contact_no}" doesn\'t exists')
    else:
        
        print('No action...')
    
    with open('student_data.dat', 'wb') as f:
        for element in data:
            dump(element, f)
    


def show_record():
    try:
        print('\n\nNAME - CONTACT_NUMBER')
        while True:
            data = load(FILE)
            for d in data:
                print(f'{d} - {data[d]}')
    except:
        print()


def show_menu():
    print(
        '1. Add Record \n' \
        '2. Search Record \n' \
        '3. Modify Record \n' \
        '4. Show record \n' \
        '5. Exit'
    )
    inp = int(input('Action [1/2/3/4/5]: '))
    if inp == 1:
        add_record()
    elif inp == 2:
        search_record()
    elif inp == 3:
        modify_record()
    elif inp == 4:
        show_record()
    elif inp == 5:
        exit_program()
    else:
        print('\nInvalid input...')



if __name__=='__main__':
    while True:
        FILE.seek(0)
        show_menu()
  
