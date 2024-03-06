# Define a function
def sum_numbers(first: int, second: int):
    """
    Returns (int) - a sum of two integers
    """
    return first + second


def add_and_subtract(sum: int, third: int):
    """
    Takes the return from the sum_numbers function(int)
    then subtracts it with the third integer
    :return: int
    """""
    return sum - third

# Read User input
f_int, s_int, t_int = int(input()), int(input()), int(input())
sum = sum_numbers(f_int, s_int)

# Print function result
print(add_and_subtract(sum, t_int))
