
# Implement a generator function
def squares(n):
    """ This func. generate the squares of all numbers from 1 to n (inclusive) """
    current = 1
    while current < n + 1:
        yield current ** 2
        current += 1


# Test code
print(list(squares(5)))

# res = squares(5)
#
# for r in res:
#     print(r)
