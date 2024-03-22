def multiply(num):
    def decorator(function):
        def wrapper(*args, **kwargs):
            number = function(*args, **kwargs)
            number *= num
            return number

        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))
