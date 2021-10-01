from datetime import datetime


def my_decorator(func):
    def wrapper():
        print("doing something before the function")
        func()
        print("doing something after the function")

    return wrapper


def not_during_day(func):
    def wrapper():
        if 18 <= datetime.now().hour <= 23:
            func()
        else:
            pass
    return wrapper


@my_decorator
def say_hello():
    print("Hi There!")


# say_hello = my_decorator(say_hello)
# say_hello()

# say_hello = not_during_day(say_hello)
# say_hello()

say_hello()
