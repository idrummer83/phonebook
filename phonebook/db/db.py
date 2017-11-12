import sqlite3
from constants import *
from validate import Validate

valid = Validate()

db = sqlite3.connect('phonebook.db.sqlite3')
cursor = db.cursor()


def act():
    while True:
        try:
            command = input('Enter your command: c(create), r(read), u(update), d(delete), e(exit) : ')
            if command == create:
                n = valid.check_name()
                p = valid.check_phone()
                cursor.execute("insert into phonebook (name,phone) values(?,?)", (n, p))
                id = cursor.lastrowid
                db.commit()
                print('your id is -- {}'.format(id))
            elif command == read:
                rd = cursor.execute('select * from phonebook')
                print(rd.fetchall())
            elif command == update:
                user_id = input('please print your id --  ')
                user_name = input('please print your name --  ')
                user_phone = input('please print your phone --  ')
                cursor.execute('update phonebook set name = ?, phone = ? where id = ?',(user_name, user_phone,user_id))
                db.commit()
                rd = cursor.execute('select * from phonebook')
                print(rd.fetchall())
            elif command == delete:
                user_id = input('please print your id --  ')
                cursor.execute('delete from phonebook where id = ?', (user_id))
                db.commit()
                rd = cursor.execute('select * from phonebook')
                print(rd.fetchall())
            elif command == exit:
                print('out from program')
                break

        except ValueError:
            print('Please choose your command')


# if __name__ == '__main__':
#     act()