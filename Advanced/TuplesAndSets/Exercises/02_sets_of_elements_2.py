# Read User input - the 2 ranges
n, m = [int(x) for x in input().split()]

# Loop n,m times and store each input in the sets
first_set = {input() for _ in range(n)}
second_set = {input() for _ in range(m)}

# Print User output - unpack the collections separated by commas
print(*first_set.intersection(second_set), sep="\n")
