from math import log


# Read the number
number = int(input())
try:
    base = int(input())  # Read the logarithm base
    print(f'{log(number, base):.2f}')  # Print to the User
except ValueError:
    print(f'{log(number):.2f}')  # Print to the User

g