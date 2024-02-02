# Initialise a dictionary to store the data
data = {}

# Save the word and their definitions into the dict
text = input().split(' | ')
for part in text:
    word, definition = part.split(': ')
    if word not in data.keys():
        data[word] = []
    data[word].append(definition)

# Teacher words
words = input().split(' | ')

# Read the command
action = input()
if action == 'Test':
    for word in words:
        if word in data.keys(): # short it
            print(f'{word}:')
            for value in data[word]:
                print(f' -{value}')
elif action == 'Hand Over':
    some_list = []
    for key in data.keys():
        some_list.append(key)
    print(' '.join(some_list))
