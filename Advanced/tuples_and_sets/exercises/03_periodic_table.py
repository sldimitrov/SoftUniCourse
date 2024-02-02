collection = set()

# Logic
for l in range(int(input())):
    for el in input().split():
        collection.add(el)

# Time complexity - O(n^2)

# Print User output
print(*collection, sep='\n')
