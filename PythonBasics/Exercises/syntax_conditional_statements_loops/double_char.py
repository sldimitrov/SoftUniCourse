# Read User input

# Logic
while True:
    string = input()
    if string == 'End':
       break
    if string == 'SoftUni':
        continue
    for index in string:
        print(index * 2, end='')
    print()
# Print User output
