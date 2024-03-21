
# Define a function
def genrange(start: int, end: int):
    """ Generate all the numbers from the start to the end (inclusive). """
    while start < end + 1:
        yield start
        start += 1


# Testcode
res = genrange(1, 10)
for r in res:
    print(r)