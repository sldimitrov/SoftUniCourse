
# Define a function
def fibonacci():
    """ Generator that generates fibonacci sequence """
    n_1, n_2 = 0, 1

    while True:
        yield n_1
        n_1, n_2 = n_2, n_1 + n_2


# Test code
generator = fibonacci()
for i in range(5):
    print(next(generator))
