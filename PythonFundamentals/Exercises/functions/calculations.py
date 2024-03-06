# Define a function
def calculations(operator: str, a: int, b: int):
    """
         This function calculate the second and the third
        parameter on base on the operator which is the
        first parameter.
            * If the operator is subtract:
                result = a - b

        Parameters: operator: str, a: int, b: int

        It calculates the result of the
        operator and returns it
    """
    if operator == 'multiply':
        return a * b
    elif operator == 'divide':
        return int(a / b)
    elif operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b
# Read User input
operator = input()
first_parameter = int(input())
second_parameter = int(input())

# Call the function and print its result
print(calculations(operator, first_parameter, second_parameter))




