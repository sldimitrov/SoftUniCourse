# Read the 2 ranges
n, m = [int(x) for x in input().split()]

# Loop r times
first_set = {input() for x in range(n)}
second_set = {input() for x in range(m)}

# Print user output
print(*(first_set.intersection(second_set)), sep="\n")