import re


# Read User input
text = input()
regex = r"(@|#)([A-Za-z]{3,})\1{2}([A-Za-z]+)\1"
mirror_words = []
# Find matches
matches = re.findall(regex, text)
length = 0

# Logic
for match in matches:
    if match[1] == match[2][::-1]:
        mirror_words.append(f'{match[1]} <=> {match[2]}')
    length += 1

# Print User output
if length > 0:
    print(f"{length} word pairs found!")
else:
    print("No word pairs found!")
if mirror_words:
    print(f'The mirror words are:')
    print(", ".join(mirror_words))
else:
    print("No mirror words!")

# Test 2

