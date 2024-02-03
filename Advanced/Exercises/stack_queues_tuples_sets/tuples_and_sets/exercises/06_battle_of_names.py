# Read User input
names = [input() for x in range(int(input()))]

# Initialise collections to store data
even_collection = set()
odd_collection = set()

# Logic
counter = 1
for name in names:
    current_sum = 0
    for el in name:
        current_sum += ord(el)

    total_sum = int(current_sum / counter)
    if total_sum % 2 == 0:
        even_collection.add(int(current_sum / counter))
    else:
        odd_collection.add(int(current_sum / counter))
    counter += 1

# Print User output
if sum(even_collection) == sum(odd_collection):
    print(*(even_collection.union(odd_collection)),sep=', ')
elif sum(even_collection) <= sum(odd_collection):
    print(*(odd_collection.difference(even_collection)),sep=', ')
else:
    print(*(even_collection.symmetric_difference(odd_collection)),sep=', ')