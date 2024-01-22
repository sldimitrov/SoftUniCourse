# Initialise a list to stack to store data
numbers = []

# Use as an alternative of if-else-statements
map_functions = {
    "1": lambda x: numbers.append(x[1]),
    "2": lambda x: numbers.pop() if numbers else None,
    "3": lambda x: print(max(numbers)) if numbers else None,
    "4": lambda x: print(min(numbers)) if numbers else None,
}

# Read User input as a range of the loop
for _ in range(int(input())):
    numbers_data = input().split()
    command = numbers_data[0]
    map_functions[command](numbers_data)

# Reverse the elements in the stack
numbers.reverse()

# Print output
print(*numbers, sep=", ")
