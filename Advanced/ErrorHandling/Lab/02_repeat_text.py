
# Read User input
text = input()

# Scenarios
try:  # input an integer number
    multiplier = int(input())
    print(text*multiplier)
except ValueError:  # if not
    print('Variable must be an integer')
