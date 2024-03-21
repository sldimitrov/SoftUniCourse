
# For loop implementation
iterable = [1, 2, 3].__iter__()

while True:
    try:
        print(next(iterable))
    except StopIteration:
        break
