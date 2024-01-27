def factorial(number):
    if not isinstance(number, int) or number < 0:
        return f"Sorry. 'number' is incorrect."

    def inner_factorial(n):
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        return fact

    return inner_factorial(number)


# print(factorial(5))

# Playing with the scope of the inner function
def a():
    def b():
        return 'Hello'
    return b


result = a()  # Expose inner function for the outer world
print(result())

# Another way to do it
print(a()())  # uglier
