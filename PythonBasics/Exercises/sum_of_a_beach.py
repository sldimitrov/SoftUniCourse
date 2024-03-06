word = input().lower()
counter = 0
target_words = ('water', 'fish', 'sun', 'sand')

for target in target_words:
    counter += word.count(target)

print(counter)