# Read User input
text = [x for x in input()]   # taking every symbol
reversed_text = ''

# Logic - loop as many times as the length of the text
for _ in range(len(text)):
    removed_symbol = text.pop()  # add the last symbol first
    reversed_text += removed_symbol

# Print User output
print(reversed_text)

