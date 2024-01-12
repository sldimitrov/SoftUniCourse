# User input
n = int(input())

# Initialise a stack to store data 
stack = []

# Logic
for n in range(n):
    line = input().split()
    if line[0] == '1':
        stack.append(int(line[1]))
    elif line[0] == '2':
        stack.pop()
    elif line[0] == '3':
        print(max(stack))
    elif line[0] == '4':
        print(min(stack))

# Print User output
print(*reversed(stack), sep=', ')

