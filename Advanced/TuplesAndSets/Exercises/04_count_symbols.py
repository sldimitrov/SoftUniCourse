# Initialise a dictionary
collection = {}

# Read the User input into the for loop
for s in input():
    if s not in collection:
        collection[s] = 0
    collection[s] += 1

# Print User output
for el, occ in sorted(collection.items()):
    print(f"{el}: {occ} time/s")