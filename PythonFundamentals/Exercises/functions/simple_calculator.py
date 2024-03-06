# Define a function
def calculator(operator, num1, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return abs(num1 - num2)
    elif operator == '*':
        return num1 * num2
    elif operator == '/' and num2 != 0:
        return int(num1 / num2)
    else:
        return 'Wrong operator or number'


# Read User input
operator = input()
first_paramater = int(input())
second_paramater = int(input())

# Call the function and get the return
result = calculator(operator, first_paramater, second_paramater)

# Print the result
print(result)
