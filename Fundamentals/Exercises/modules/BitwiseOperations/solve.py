import math
from math import floor
# Define a function
def solve(number, digit):
    count = 0
    while number > 0:
        remainder = number % 2
        number = math.floor(number / 2)

        if remainder == digit:
            count += 1
    print(count)


solve(20, 0)

