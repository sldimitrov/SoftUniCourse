# Using a list comprehension to take all chars in a list/
# to remove spaces in the input
symbols = [character for character in input() if character != ' ']

# Initialise a dictionary
some_dict = {}

# Iterate through the list
for symbol in symbols:
    if symbol not in some_dict:
        # create a key(symbol) with 0 value
        some_dict[symbol] = 0
    # else:
    # Increase the value by 1
    some_dict[symbol] += 1

# Iterate through the dict items
# Printing key, value on a single line
for key, value in some_dict.items():
    print(f"{key} -> {value}")