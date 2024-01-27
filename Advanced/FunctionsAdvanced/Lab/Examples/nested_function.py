def factorial(number):
    if not isinstance(number, int) or number < 0:
        return f"Sorry. 'number' is incorrect."

    def inner_factorial(n):
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        return fact
    return inner_factorial(number)

print(factorial(5))