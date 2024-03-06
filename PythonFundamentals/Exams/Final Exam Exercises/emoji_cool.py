import re


text = input()

# Threshold find
number_regex = r"\d"
numbers = re.findall(number_regex, text)
threshold = 1
for num in numbers:
    threshold *= int(num)

# Find the emojis
regex = r"::[A-Z][a-z]{2,}::|\*\*[A-Z][a-z]{2,}\*\*"
emojis = re.findall(regex, text)

# Find the cool ones
cool_emojis = []
for emoji in emojis:
    ascii_counter = 0
    for symbol in emoji:
        if symbol.isalpha():
            ascii_counter += ord(symbol)
    if ascii_counter > threshold:
        cool_emojis.append(emoji)

print(f'Cool threshold: {threshold}')
print(f'{len(emojis)} emojis found in the text. The cool ones are:')
for emoji in cool_emojis:
    print(emoji)
