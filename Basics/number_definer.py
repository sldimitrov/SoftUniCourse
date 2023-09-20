# Read User input
number = float(input())
# Logic
if number == 0:
    print('zero')
elif number > 0:
    if abs(number) > 1000000:
        print('large', end=' ')
    elif 0 < abs(number) < 1:
        print('small', end=' ')
    print('positive')
elif number < 0:
    if abs(number) > 1000000:
        print('large', end=' ')
    elif 0 < abs(number) < 1:
        print('small', end=' ')
    print('negative')
# Print User output