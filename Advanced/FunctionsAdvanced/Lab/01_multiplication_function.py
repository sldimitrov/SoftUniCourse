# Define Function
def multiply(*args):
    total_count = 1
    for i in args:
        total_count = total_count * i
    return total_count


# Test Code
print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
