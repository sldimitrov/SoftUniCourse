def tags(tag):
    def function(func):
        def wrapper(*args):
            return f"<{tag}>{func(*args)}</{tag}>"

        return wrapper
    return function


@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))
