from crud import crud
from constants import *
from validate import Validate

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
            elif command == to_csv:
                f = crud.read_file()
                crud.write_to_cvs(f)
            elif command == exit:
                print('out from program')
                break

        except ValueError:
            print('Please choose your command')


if __name__ == '__main__':
    action()