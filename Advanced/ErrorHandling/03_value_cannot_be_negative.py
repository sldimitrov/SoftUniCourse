# Initialise a class to be used as an exception

class ValueCannotBeNegative(Exception):
    pass


while True:
    number = int(input())
    if number < 0:  # if number is negative
        # throws an exception and stops the program
        raise ValueCannotBeNegative
