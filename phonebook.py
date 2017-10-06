import configparser, json, csv

def read_conf(a, b):
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config[a][b]

name_file = read_conf('FILE', 'filename')
format_file = read_conf('FILE','format')
format_csv = read_conf('FILE','csv_format')

file = "{}.{}".format(name_file,format_file)
csv_file = "{}.{}".format(name_file,format_csv)

create = 'c'
read = 'r'
update = 'u'
delete = 'd'
csv = 's'
exit = 'e'

class Json:
    def read(self):
        with open(file, 'r') as f:
            self.file_read = json.loads(f.read())
            return self.file_read
    def write(self, content):
        with open(file, "w") as f:
            self.file_write = f.write(json.dumps(content, file))


if read_conf('DEFAULT','json') == 'json':
    db = Json() #class
else:
    db = csv() #class


class Crud:
    def __init__(self, db):
        try:
            self.pb = db.read()
        except:
            self.pb = {}

    def write_to_file(self, name, phone):
        self.pb[name] = phone
        db.write(self.pb)

    def read_file(self):
        print(self.pb)

    def remove_data(self, item):
        items = self.pb
        del items[item]
        db.write(items)

    def update_data(self):
        change_name = input('print name: ')
        change_phone = input('print phone: ')
        items = self.pb
        items[change_name] = change_phone
        db.write(items)


crud = Crud(db)

def save_csv():
    try:
        with open(file, 'r') as f:
            aa = json.loads(f.read())
            if len(aa) > 0:
                with open('mycsvfile.csv', 'w') as f:
                    w = csv.Writer(f)
                    for r in aa:
                        w.writerows(aa.items(r))
    except:
        pass

    # def check_name():
    #     name = input('name: ')
    #     while len(name) < 3:
    #         name = input('minimal 3 letters, please type name: ')
    #     return name
    #
    # def check_phone():
    #     phone = input('phone: ')
    #     while len(phone) < 6:
    #         phone = input('minimal 6 numbers, please type phone: ')
    #     return phone


class Validate:
    def check_name(self):
        self.name = input('name: ')
        while len(self.name) < 3:
            self.name = input('minimal 3 letters, please type name: ')
        return self.name

    def check_phone(self):
        self.phone = input('phone: ')
        while len(self.phone) < 6:
            self.phone = input('minimal 6 numbers, please type phone: ')
        return self.phone

valid = Validate()

# controller
def action():
    while True:
        try:
            command = input('Enter your command: c(create), r(read), u(update), d(delete), s(save to csv), e(exit) : ')
            if command == create:
                n = valid.check_name()
                p = valid.check_phone()
                crud.write_to_file(n,p)
            elif command == read:
                crud.read_file()
            elif command == update:
                crud.update_data()
            elif command == delete:
                item = input('are you shure? type your "name": ')
                crud.remove_data(item)
            elif command == csv:
                save_csv()
            elif command == exit:
                print('out from program')
                break

        except ValueError:
            print('Please choose your command')

action()