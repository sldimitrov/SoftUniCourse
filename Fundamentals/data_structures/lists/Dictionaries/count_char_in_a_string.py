text = [character for character in input() if character != ' ']

some_dict = {}

for char in text:
    if char not in some_dict:
        some_dict[char] = 0
    some_dict[char] += 1

for word in some_dict:
    print(f"{word} -> {some_dict[word]}")