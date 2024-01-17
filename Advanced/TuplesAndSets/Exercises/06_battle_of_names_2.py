# Initialise collections to store data
even_set = set()
odd_set = set()

# Read User Input in for loop
for row in range(1, int(input()) + 1):
    ascii_sum = sum(ord(el) for el in input()) // row

    if ascii_sum % 2 == 0:
        even_set.add(ascii_sum)
    else:
        odd_set.add(ascii_sum)

# Calculate the sum of each set
even_set, odd_set = sum(even_set), sum(odd_set)

# Print User output
if even_set == odd_set:
    print(*(even_set.union(odd_set)),sep=', ')
elif even_set <= odd_set:
    print(*(odd_set.difference(even_set)),sep=', ')
else:
    print(*(even_set.symmetric_difference(odd_set)),sep=', ')