# Read Parameters of the matrix
n_rows, n_cols = [int(x) for x in input().split()]

start = ord('a')

for row in range(n_rows):
    for col in range(n_cols):
        print(chr(start + row), sep=' ', end=' ')

    print()
