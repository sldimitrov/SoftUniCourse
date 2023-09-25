# word = input()

# print(word[::-1])

word = input()

for i in range(len(word) - 1, -1 , -1):
    print(word[i], end='')
    # Slice notation
# my_string = 'I\'m the best ever'
# reversed_string = my_string[::-1]
# print(reversed_string)