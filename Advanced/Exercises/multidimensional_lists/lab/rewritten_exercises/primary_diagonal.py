# Read the rows
rows = int(input())

# Initialise variables
matrix = []
primary_diagonal = []

# Logic
for row in range(rows):
    line = input().split()
    matrix.append(line)
    primary_diagonal.append(int(line[row]))

print(sum(primary_diagonal))
