import configparser, json, ast
config = configparser.ConfigParser()
config.read('config.ini')

name_file = config['FILE']['filename']
format_file = config['FILE']['format']

file = "{}.{}".format(name_file,format_file)

def write_to_file(t):
    with open("{}.{}".format(name_file,format_file), "w") as file:
        json.dump("{}".format(t), file)

def read_file():
    with open(file, "r") as f:
        print(f.read())

def remove_data(item):
    with open(file, 'r') as f:
        a = ast.literal_eval(json.loads(f.read()))
    del a[item]
    with open(file, 'w') as asd:
        asd.write(json.dumps(a))



create = 'c'
read = 'r'
update = 'u'
delete = 'd'
exit = 'e'

contacts = {}

def check_name():
    name = input('name: ')
    while len(name) < 3:
        name = input('minimal 3 letters, please type name: ')
    return name

def check_phone():
    phone = input('phone: ')
    while len(phone) < 6:
        phone = input('minimal 6 numbers, please type phone: ')
    return phone

def action():
    while True:
        try:
            command = input('Enter your command: ')
            if command == create:
                n = check_name()
                p = check_phone()
                contacts[n] = p
                c = str(contacts)
                write_to_file(c)
                print('your contacts are: {}'.format(contacts))
            elif command == read:
                read_file()
            elif command == update:
                change_name = input('print name: ')
                change_phone = input('print phone: ')
                contacts[change_name] = change_phone
                print('your contacts are: {}'.format(contacts))
            elif command == delete:
                motion = input('are you shure? type your "name": ')
                remove_data(motion)
            elif command == exit:
                print('out from program')
                break

        except ValueError:
            print('Please choose your command')

action()