def store_results(func):
    def wrapper(*args, **kwargs):
        with open(f"results.txt", "a") as file:
            # String documentation of the function name and results
            info = f"Function {func.__name__} was called. Result: {func(*args, **kwargs)}\n"

            # Write the info into the file
            file.write(info)

    return wrapper


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
