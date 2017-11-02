import multiprocessing
import urllib.request

def req(url):
    r = urllib.request.urlopen(url)
    return len(r.read())

p = multiprocessing.Pool(5)
print(p.map(req, ['http://wikipedia.org']*10))




# a=0
# q = multiprocessing.Queue()
#
# def f():
#     global a
#     for i in range(250000):
#         a += 1
#     q.put(a)
#
#
# for i in range(4):
#     p = multiprocessing.Process(target=f)
#     p.start()
#
#
# for i in range(4):
#     a += q.get()
#
# print(a)






# import time
#
# def hello():
#     print('hello')
#     for i in range(1000000):
#         for j in range(1000000):
#             pass
#             # time.sleep(600)
#
#
# for i in range(10):
#     p = multiprocessing.Process(target=hello)
#     p.start()








# import threading
# import urllib.request
#
# s = 0
# l = threading.Lock()
#
#
# def req():
#     global s
#     r = urllib.request.urlopen('http://itea.ua')
#     l.acquire()
#     s += len(r.read())
#     l.release()
#     # print(len(r.read()))
#
# for i in range(20):
#     t = threading.Thread(target=req)
#     t.start()






# import time
#
# a = 0
# l = threading.Lock()
#
# def f():
#     global a
#     for i in range(500000):
#         # l.acquire()
#         a += 1
#         # l.release()
#     # print('hello', i)
#
# ts = []
#
# for i in range(2):
#     t = threading.Thread(target=f)
#     ts.append(t)
#     t.start()
#
#
# for t in ts:
#     t.join()
#
# # time.sleep(1)
# print(a)