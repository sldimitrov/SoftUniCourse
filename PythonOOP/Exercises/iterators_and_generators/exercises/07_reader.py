
# Define a function
def read_next(*args):
    length = len(args)
    counter = 0

    while counter < length:
        yield from args[counter]
        counter += 1


# Test code
for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')
