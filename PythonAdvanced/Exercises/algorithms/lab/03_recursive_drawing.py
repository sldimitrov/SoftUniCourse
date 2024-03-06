
def recursive_drawing(n: int):

    # Base case
    if n == 0:
        return 1

    # Sinking below
    print('*' * n)

    # Recursive case
    recursive_drawing(n - 1)

    # Surfacing
    print('#' * n)


# Read User input
number = int(input())

# Call the function above
recursive_drawing(number)
