# Define a function
def characters_in_range(char1: str, char2: str):
    """
    This function works with two parameters which are borders.
    On base of them we need to print the symbols between with
    their asci representation
    :return: str
    """
    list_with_sym = []
    for i in range(ord(char1) + 1, ord(char2)):
        list_with_sym.append(chr(i))
    return list_with_sym


# Read User input
first_char = input()
second_char = input()
list_with_symbols = characters_in_range(first_char, second_char)

# Print function return
for symbol in list_with_symbols:
    print(symbol,end=' ')
