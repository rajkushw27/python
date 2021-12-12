import time


def time_decorator(func):
    def inner_function(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        # time.sleep(1)
        print(f'Execution time {time.time() - start}')

    return inner_function


@time_decorator
def print_table(num):
    table = [num * i for i in range(1, 11)]
    print(table)


@time_decorator
def multiply_number():
    for i in range(1, 435):
        for j in range(1, 4654):
            print(i * j)


print_table(7)
multiply_number()
