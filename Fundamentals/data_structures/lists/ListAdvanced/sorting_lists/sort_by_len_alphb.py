a = input().split()

# Sorting first by length and then by alphabetic numeric
a = sorted(a, key = lambda x: (len(x), x))
print(a)