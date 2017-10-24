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


class Json:
    def read(self):
        with open(file, 'r') as f:
            self.file_read = json.loads(f.read())
            return self.file_read
    def write(self, content):
        with open(file, "w") as f:
            self.file_write = f.write(json.dumps(content, file))


def jsonorcsv():
    if read_conf('DEFAULT', 'json') == 'json':
        db = Json()  # class
        return db
    else:
        db = csv()  # class
        return db