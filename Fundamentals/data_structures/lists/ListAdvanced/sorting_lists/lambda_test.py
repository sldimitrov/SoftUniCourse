# Lambda for finding power of numbers
numbers = [1, 2, 3, 4, 5]
square_numbers = list(map(lambda x: x*x, numbers))
print(square_numbers)

# Lambda for string.lower()
strings = ['Pesho', 'gosho']
lower_strings = list(map(lambda x: x.lower(), strings))
print(lower_strings)

upper_strings = list(map(lambda x: x.upper(), strings))
print(upper_strings)

capitalise_strings = list(map(lambda x: x.capitalize(), strings))
print(capitalise_strings)