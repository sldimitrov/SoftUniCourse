# Read User input
expression = input()

# Initialise a list to store data
opening_braces = []

# Logic
counter = 0  # Indicates the index
for s in expression:
    if s == '(':  # starts a set
        opening_braces.append(counter)
    elif s == ')':  # ends it
        start = opening_braces.pop()
        end = counter + 1
        # Print User output
        print(expression[start:end])
    counter += 1
