n = int(input())


def print_top_part(size):
    for row in range(1, size + 1):
        print(" " * (size - row), '* ' * row)


def print_bottom_part(size):
    for row in range(size - 1, 0, -1):
        print(" " * (size - row), '* ' * row)


def create_phombus(n):
    print_top_part(n)
    print_bottom_part(n)


create_phombus(n)