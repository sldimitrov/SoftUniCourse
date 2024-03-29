
# Define a function
def genrange(start: int, end: int, step=0):
    """ Generate all the numbers from the start to the end (inclusive). """
    while start < end + 1:
        yield start
        start += 1 + (step - 1)


# Testcode
res = genrange(0, 10, 2)
for r in res:
    print(r)