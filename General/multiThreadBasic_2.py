from threading import Lock, Thread
import threading

a = 0


def halfMillionSum(lock):
    global a
    for i in range(500001):
        lock.acquire()
        a += i
        lock.release()


def halfMillionToMillionSum(lock):
    global a
    for i in range(500001, 1000001):
        lock.acquire()
        a += i
        lock.release()


lock = threading.Lock()
t1 = threading.Thread(target=halfMillionSum, args=[lock])
t2 = threading.Thread(target=halfMillionToMillionSum, args=[lock])
t1.start()
t2.start()

t1.join()
t2.join()

print(a)
