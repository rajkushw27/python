import time
import threading


def counter(count):
    while count >= 0:
        count -= 1


count = 500000000

start = time.time()
counter(count)
end = time.time()

print(end - start)

print("=================================Threading=========================")

count = 500000000

start = time.time()

t1 = threading.Thread(target=counter, args=[count//2])
t2 = threading.Thread(target=counter, args=[count//2])

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(end - start)


def counter(count):
    while count >= 0:
        count -= 1


count = 500000000

start = time.time()
counter(count)
end = time.time()

print(end - start)

print("=================================Threading=========================")

count = 500000000

start = time.time()

t1 = threading.Thread(target=counter, args=[count//2])
t2 = threading.Thread(target=counter, args=[count//2])

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(end - start)
