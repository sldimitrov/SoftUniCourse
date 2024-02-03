from functools import reduce


# Define a function
# def operate(operator, *args):
#     if operator == "+":
#         return reduce(lambda x, y: x+y, args)
#     elif operator == "-":
#         return reduce(lambda x, y: x-y, args)
#     elif operator == "*":
#         return reduce(lambda x,y: x-y, args)
#     elif operator == "/":
#         return reduce(lambda x,y: x/y, args)


# do NOT do use in real-live-project
# be aware of dropping the data base
def operate(operator, *args):
    return reduce(lambda x,y: eval(f"{x}{operator}{y}"), args)