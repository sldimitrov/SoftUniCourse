list_of_chars = input().split(', ')

dictionary = {}

for character in list_of_chars:
    dictionary[character] = ord(character)
print(dictionary)
