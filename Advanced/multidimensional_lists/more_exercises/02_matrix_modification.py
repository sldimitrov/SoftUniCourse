# Read User input
n = int(input())

matrix = [[int(x) for x in input().split()] for x in range(n)]

# Logic
command = input().split()
while command[0] != "END":
    command_type, r, c, value = command[0], int(command[1]), int(command[2]), int(command[3])

    if 0 <= r < n and 0 <= c < n:
        if command_type == "Add":
            matrix[r][c] += value
        elif command_type == "Subtract":
            matrix[r][c] -= value

    else:
        print('Invalid coordinates')

    command = input().split()

# Print User output
[print(*row) for row in matrix]
