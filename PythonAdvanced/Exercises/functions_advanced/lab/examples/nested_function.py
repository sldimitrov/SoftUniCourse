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
# def a():
#     def b():
#         return 'Hello'
#     return b


# result = a()  # Expose inner function for the outer world
# print(result())

# # Another way to do it
# print(a()())  # uglier


# Lexical closures examples
def a(num):
    def b():
        print(num)

    return b()


a(10)


# Ex: 2
def greeting(name):
    hello = "Hello, "

    def say_hi():
        return hello + name

    return say_hi  # return a pointer to the inner func.


print(greeting("Peter")())  # syntax used to call the inner func.
# also used within the decorators # TODO: check decorators
