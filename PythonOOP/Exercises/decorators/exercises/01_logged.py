def logged(func):
    def wrapper(*args):
        result = func(*args)
        function = f"{func.__name__}{args}"

        info = f"you called {function}\n" \
               f"it returned {result})"

        return info

    return wrapper


@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))
