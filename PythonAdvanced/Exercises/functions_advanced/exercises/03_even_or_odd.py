# Define a function
def even_odd(*args) -> list:
    if args[-1] == 'even':
        even_numbers = [x for x in args[:-1] if x % 2 == 0]
        return even_numbers
    elif args[-1] == 'odd':
        odd_numbers = [x for x in args[:-1] if x % 2 != 0]
        return odd_numbers


# Test code
print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
