import unittest


def even_parameters(func):
    def wrapper(*args):
        for number in args:
            if isinstance(number, int):
                if number % 2 == 0:
                    continue

            return f"Please use only even numbers!"

        else:
            return func(*args)

    return wrapper


@even_parameters
def add(a, b):
    return a + b
