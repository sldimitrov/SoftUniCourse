size = int(input())
matrix = [list(input()) for _ in range(size)]

positions = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (1, 2),
)

removed_knights = 0

while True:
    max_attacks = 0
    knights_with_most_attacks_pos = []

    for row in range(size):
        for col in range(size):

            if matrix[row][col] == 'K':
                current_attacks = 0
                for pos in positions:
                    pos_1 = row + pos[0]
                    pos_2 = col + pos[1]

                    if 0 <= pos_1 < size and 0 <= pos_2 < size:
                        if matrix[pos_1][pos_2] == 'K':
                            current_attacks += 1

                if current_attacks > max_attacks:
                    knights_with_most_attacks_pos = [row, col]
                    max_attacks = current_attacks

    if knights_with_most_attacks_pos:
        r, c = knights_with_most_attacks_pos
        matrix[r][c] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)

