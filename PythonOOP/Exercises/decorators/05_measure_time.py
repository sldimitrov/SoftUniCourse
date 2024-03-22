from time import time
from time import sleep


def measure_time(function):
    def wrapper(*args, **kwargs):
        start = time()
        result = function(*args, **kwargs)
        end = time()
        print(end - start)
        return result
    return wrapper


@measure_time
def time_stop(coll: list):
    for a in coll:
        print(a)
        sleep(1)


time_stop([1, 2, 3])






