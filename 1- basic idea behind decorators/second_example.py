from datetime import datetime


def stop_watch(func):
    def wrapper():
        start_time = datetime.now()
        func()
        end_time = datetime.now()
        print(end_time - start_time)

    return wrapper


def counter():
    for i in range(5000):
        print(i)


counter = stop_watch(counter)
counter()
