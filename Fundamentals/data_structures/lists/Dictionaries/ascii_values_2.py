# Read User input
characters = input().split(', ')

# Take the ASCII representation of the characters in the list above
# using list comprehension
ascii_char_representation = [ord(x) for x in characters]

# Zip the character with their ascii representations in a dict
dictionary = dict(zip(characters, ascii_char_representation))

# Print the dict
print(dictionary)