from datetime import datetime


def stop_watch(func):
    def wrapper():
        start_time = datetime.now()
        func()
        end_time = datetime.now()
        print(end_time - start_time)

    return wrapper


@stop_watch
def counter():
    for i in range(100):
        print(i)


counter()
