import socket
from controller import action

# print(constants)
s = socket.socket()
s.bind(('127.0.0.1', 5000))
s.listen(5)
print('wait for connect')
c, a = s.accept()
print('connect', a)
data = c.recv(1024)
zzz = action(data)
print('data --',data)
c.sendall(zzz)
c.close()
s.close()