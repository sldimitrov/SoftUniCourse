# Define a function
def calculate_the_factorial(some_number: int)-> int:
    for current_number in range(1, some_number):
        some_number *= current_number
    return some_number

# Read User input
first_number = int(input())
second_number = int(input())

# Call out the function
first_factorial = calculate_the_factorial(first_number)
second_number = calculate_the_factorial(second_number)
result = first_factorial / second_number

# Print the result
print(f'{result:.2f}')
