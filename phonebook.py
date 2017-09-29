
create = 'c'
read = 'r'
update = 'u'
delete = 'd'
exit = 'e'

contacts = {}

def check_name(name):
    while len(name) < 3:
        n = input('minimal 3 letters, please type name: ')
        if len(n) >= 3:
            return n

def check_phone(phone):
    while len(phone) < 6:
        p = input('minimal 6 numbers, please type phone: ')
        if len(p) >= 6:
            return phone

def action():
    while True:
        try:
            command = input('Enter your command: ')
            if command == create:
                name = input('name: ')
                n = check_name(name)
                phone = input('phone: ')
                p = check_phone(phone)
                contacts[n] = p
                print('your contacts are: {}'.format(contacts))
            elif command == read:
                print(contacts)
            elif command == update:
                change_name = input('print name: ')
                change_phone = input('print phone: ')
                contacts[change_name] = change_phone
                print('your contacts are: {}'.format(contacts))
            elif command == delete:
                motion = input('are you shure? type your "name": ')
                if motion in contacts:
                    del contacts[motion]
                    print(contacts)
            elif command == exit:
                print('out from program')
                break

        except ValueError:
            print('Please choose your command')

action()