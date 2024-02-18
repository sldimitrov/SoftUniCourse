
def recursive_factorial(n: int):

    # Base case - Ending the recursive call
    if n == 1:
        return 1

    # Recursive call - Потапяне
    total_sum = n * recursive_factorial(n - 1)

    # Изплуване
    return total_sum


# Read User input
number = int(input())

# Call the function and print its result
print(recursive_factorial(number))
