# Read User input
length_of_sets = [int(x) for x in input().split()]

# Initialise collections
first_set = set()
second_set = set()

# Logic
for _ in range(length_of_sets[0]):
    number = int(input())
    first_set.add(number)

for _ in range(length_of_sets[1]):
    number = int(input())
    second_set.add(number)

# Print the intersection of the two sets
intersection_of_sets = first_set & second_set
print(*intersection_of_sets, sep='\n')