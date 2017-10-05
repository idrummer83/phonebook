import configparser, json, csv
config = configparser.ConfigParser()
config.read('config.ini')

name_file = config['FILE']['filename']
format_file = config['FILE']['format']
format_csv = config['FILE']['csv_format']

file = "{}.{}".format(name_file,format_file)
csv_file = "{}.{}".format(name_file,format_csv)

create = 'c'
read = 'r'
update = 'u'
delete = 'd'
csv = 's'
exit = 'e'

contacts = {}
csv_columns = ['Name','Phone']

def write_to_file(a, b):
    try:
        with open(file, 'r') as f:
            aa = json.loads(f.read())
            if aa:
                aa[a] = b
                with open(file, "w") as f:
                    f.write(json.dumps(aa, file))
    except:
        contacts[a] = b
        with open(file, "w") as f:
            f.write(json.dumps(contacts, file))

def read_file():
    with open(file, "r") as f:
        print(f.read())

def remove_data(item):
    with open(file, 'r') as f:
        a = json.loads(f.read())
    del a[item]
    with open(file, 'w') as asd:
        asd.write(json.dumps(a))

def update_data():
    change_name = input('print name: ')
    change_phone = input('print phone: ')
    with open(file, 'r') as f:
        a = json.loads(f.read())
    a[change_name] = change_phone
    with open(file, 'w') as asd:
        asd.write(json.dumps(a))

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

def save_csv():
    try:
        with open(file, 'r') as f:
            aa = json.loads(f.read())
            if aa:
                with open('mycsvfile.csv', 'w') as f:
                    w = csv.Writer(f)
                    w.writerows(aa.items())
    except:
        pass


def action():
    while True:
        try:
            command = input('Enter your command: c(create), r(read), u(update), d(delete), s(save to csv), e(exit) : ')
            if command == create:
                n = check_name()
                p = check_phone()
                write_to_file(n, p)
            elif command == read:
                read_file()
            elif command == update:
                update_data()
            elif command == delete:
                motion = input('are you shure? type your "name": ')
                remove_data(motion)
            elif command == csv:
                save_csv()
            elif command == exit:
                print('out from program')
                break

        except ValueError:
            print('Please choose your command')

action()