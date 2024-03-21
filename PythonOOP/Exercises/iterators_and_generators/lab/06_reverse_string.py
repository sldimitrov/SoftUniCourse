
# Define function
def reverse_text(string: str):
    """ Receives a string and yields all string characters on one line in reversed order. """
    count = len(string) - 1
    while count >= 0:
        yield string[count]
        count -= 1


# Testcode
text = "abcd"
reversed_text = reverse_text(text)

for letter in reversed_text:
    print(letter, end='')
