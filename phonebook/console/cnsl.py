
def ask(a):
    if a == 'shure':
        item = input('are you shure? type your "name": ')
        return item

def out(a):
    if a == 'out':
        print('out from program')


def start(a):
    if a == 'start':
        command = input('Enter your command: c(create), r(read), u(update), d(delete), s(save to csv), e(exit) : ')
        return command