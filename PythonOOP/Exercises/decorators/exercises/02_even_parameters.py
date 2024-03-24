def even_parameters(func):
    def wrapper(*args):
        numeric_values = [v for v in args if str(v).isnumeric()]
        even_numbers = [v for v in numeric_values if v % 2 == 0]

        if len(even_numbers) == len(args):
            return func(*args)
        else:
            return "Please use only even numbers!"

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))
