from itertools import permutations


def possible_permutations(elements):
    for el in permutations(elements):
        yield list(el)


# Test code
[print(n) for n in possible_permutations([1, 2, 3])]
