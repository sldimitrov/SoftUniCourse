# Read User input
n = int(input())
# Logic
for i in range(n):
    number = int(input())
    if number == 88:
        print('Hello')
    elif number == 86:
        print('How are you?')
    elif number < 88 and number != 86:
        print('GREAT!')
    else:
        print('Bye')
# Print User output