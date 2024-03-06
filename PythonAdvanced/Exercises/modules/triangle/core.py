
def print_top(n):
    for row in range(n):
        for num in range(1, row+2):
            print(num, end=' ')
        print()


def print_bottom(n):
    for r in range(n - 1):
        for n in range(1, n):
            print(n,end=' ')
        print()

