def valid_range(value, limit) -> bool:
    return 0 <= value < limit


def move(direction, r, c):
    if direction == 'up' and valid_range(r-1, row):
        return r-1, c
    elif direction == 'down' and valid_range(r+1, row):
        return r+1, c
    elif direction == 'left' and valid_range(c-1, col):
        return r, c-1
    elif direction == 'right' and valid_range(c+1, col):
        return r, c+1
    return None, None


row, col = [int(x) for x in input().split()]
matrix = []
start_row, start_col = None, None
boy_row, boy_col = None, None

for line in range(row):
    symbols = list(input())
    matrix.append(symbols)
    if 'B' in symbols:
        boy_row = line
        boy_col = matrix[line].index('B')
        start_row = boy_row
        start_col = boy_col


while True:
    command = input()
    next_row, next_col = move(command, boy_row, boy_col)
    if next_col is None or next_col is None:
        print("The delivery is late. Order is canceled.")
        matrix[start_col][start_row] = ' '
        break
    if matrix[next_row][next_col] == '*':
        continue

    elif matrix[next_row][next_col] == 'A':
        matrix[boy_row][boy_col] = '.'
        boy_row, boy_col = next_row, next_col
        matrix[boy_row][boy_col] = 'P'
        print("Pizza is delivered on time! Next order...")
        matrix[start_row][start_col] = 'B'
        break

    if matrix[next_row][next_col] == 'P':
        matrix[boy_row][boy_col] = '.'
        boy_row, boy_col = next_row, next_col
        matrix[next_row][next_col] = 'R'
        print("Pizza is collected. 10 minutes for delivery.")
        continue

    elif not matrix[boy_row][boy_col] == 'R':
        matrix[boy_row][boy_col] = '.'
    boy_row, boy_col = next_row, next_col
    matrix[boy_row][boy_col] = '.'

[print(''.join(row)) for row in matrix]
