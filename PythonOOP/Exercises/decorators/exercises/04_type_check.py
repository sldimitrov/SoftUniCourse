
def type_check(type):
    def function(func):
        def wrapper(*args, **kwargs):
            if isinstance(*args, type):
                return func(*args, **kwargs)

            return "Bad Type"

        return wrapper
    return function


@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))
