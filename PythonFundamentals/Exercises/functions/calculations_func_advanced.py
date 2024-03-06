# Define a function
def calculations(operator: str, a: int, b: int):
    """
    This function uses an operator to make calculations
    between the numbers a and b

    :return: the result from the operation
    """
    return {
        "multiply": a * b,
        "divide": int(a / b),
        "add": a + b,
        "subtract": a - b,
    }.get(operator)

# Read User input
operator = input()
a = int(input())
b = int(input())

# Call the function and print its result
print(calculations(operator, a, b))