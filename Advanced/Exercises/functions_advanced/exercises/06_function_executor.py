# Define a function
def func_executor(*funcs_data) -> str:
    result = []

    for func, args in funcs_data:
        result.append(f"{func.__name__} - {func(*args)}")

    return '\n'.join(result)


# Test Code
def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
