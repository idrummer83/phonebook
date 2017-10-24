import configparser, csv
from serialiser.format import read_conf, Json, Csv

read_conf = read_conf

def jsonorcsv():
    if read_conf('DEFAULT', 'json') == 'json':
        db = Json()  # class
        return db
    else:
        db = csv()  # class
        return db