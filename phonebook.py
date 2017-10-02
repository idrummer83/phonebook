import configparser, json, csv
config = configparser.ConfigParser()
config.read('config.ini')

name_file = config['FILE']['filename']
format_file = config['FILE']['format']

file = "{}.{}".format(name_file,format_file)

def write_to_file(t):
    with open(file, "w") as f:
        f.write(json.dumps(t, file))

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

def save_csv():
    with open(file, 'r') as f:
        a = json.loads(f.read())
    with open('phonebook.csv', 'w') as f:
        writer = csv.writer(f)
        for key, value in a.items():
            writer.writerow([key, value])
        # writer = csv.DictWriter(f, fieldnames=csv_columns)
        # writer.writeheader()
        # for data in a:
        #     writer.writerow(data)


create = 'c'
read = 'r'
update = 'u'
delete = 'd'
csv = 's'
exit = 'e'

contacts = {}
csv_columns = ['Name','Phone']

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
            command = input('Enter your command: c(create), r(read), u(update), d(delete), s(save to csv), e(exit) : ')
            if command == create:
                n = check_name()
                p = check_phone()
                contacts[n] = p
                write_to_file(contacts)
                print('your contacts are: {}'.format(contacts))
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