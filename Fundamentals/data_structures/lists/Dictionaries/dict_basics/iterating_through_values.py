squares = {1: 1, 2: 4, 3: 9}
for value in squares.values():
    print(value, end='')
print() # blank line

# We can also use the keys to get the values
squares = {1: 1, 2: 4, 3: 9}
for key in squares.keys():
    print(squares[key], end=' ')