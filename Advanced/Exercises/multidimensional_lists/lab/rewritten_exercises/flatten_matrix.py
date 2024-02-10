rows = int(input())

matrix = [input().split(', ') for x in range(rows)]

flattened = [int(num) for row in matrix for num in row]

print(flattened)

