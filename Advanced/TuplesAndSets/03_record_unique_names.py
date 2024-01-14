# Read User input
n = int(input())

# Initialize an empty set
names = set()

# Logic
for _ in range(n):
    name = input()
    names.add(name)  # Add names into set

# Print User Output
print('\n'.join(names))