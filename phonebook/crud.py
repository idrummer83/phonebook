import csv
from saveto.saveto import jsonorcsv, csv_file

db = jsonorcsv()

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
        return self.pb

    def write_to_cvs(self, d):
        with open(csv_file, 'w') as csvfile:
            fieldnames = ['name', 'phone']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for i, k in d.items():
                writer.writerow({'name': i, 'phone': k})

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
