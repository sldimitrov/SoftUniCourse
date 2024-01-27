from functools import reduce


# Define a function
def operate(operator, *args):
    if operator == "+":
        return reduce(lambda x, y: x+y, args)
    elif operator == "-":
        return reduce(lambda x, y: x-y, args)
    elif operator == "*":
        return reduce(lambda x,y: x-y, args)
    elif operator == "/":
        return reduce(lambda x,y: x/y, args)
