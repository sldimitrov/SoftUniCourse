
def linear_factorial(n):
    """
    This function returns the factorial of a positive number.
    :param n: integer number
    :return: int number
    """

    # Initialise a total sum counter
    total_sum = 1

    # Main loop
    for i in range(n, 1, -1):  # Time complexity - O(n)
        total_sum *= i

    # Return statement
    return total_sum


# Call the function above and pass arg
print(linear_factorial(5))  # print the returned value


def recursive_factorial(n):
    """
    A function that returns the factorial of a number using recursion
    :param n: int
    :return: integer number
    """

    # Base case - Дъно
    if n == 1:  # Изплуване
        return 1

    # Recursion case
    total_sum = n * recursive_factorial(n - 1)  # Потапяне

    return total_sum


print(recursive_factorial(5))
