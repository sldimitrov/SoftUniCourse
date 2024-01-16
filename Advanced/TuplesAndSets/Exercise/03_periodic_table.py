# Read User input
n_lines = int(input())

collection = set()
# Logic - Algorithm O(n^2) BAD
for l in range(n_lines):
    line = input().split()
    for el in line:
        collection.add(el)

# Print User output
print(*collection, sep='\n')