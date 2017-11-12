from pymongo import MongoClient
from constants import *
from validate import Validate

valid = Validate()

client = MongoClient()
db = client.phonebook


def act():
    while True:
        try:
            command = input('Enter your command: c(create), r(read), u(update), d(delete), e(exit) : ')
            if command == create:
                n = valid.check_name()
                p = valid.check_phone()
                user = {'phone': p, 'name': n}
                db.phonebook.insert(user)
            elif command == read:
                readbase = db.phonebook.find()
                print('All data from Database')
                for u in readbase:
                    print(u)
            elif command == update:
                user_phone = input('please print your phone --  ')
                user_new_phone = input('please print your new phone --  ')
                db.phonebook.update({'phone': user_phone}, {'$set': {'phone': user_new_phone}})
                readbase = db.phonebook.find()
                print('All data from Database')
                for u in readbase:
                    print(u)

            elif command == delete:
                user_phone = input('please print your phone --  ')
                db.phonebook.remove(
                    {'phone': user_phone}
                )
                readbase = db.phonebook.find()
                print('All data from Database')
                for u in readbase:
                    print(u)
            elif command == exit:
                print('out from program')
                break

        except ValueError:
            print('Please choose your command')


if __name__ == '__main__':
    act()
