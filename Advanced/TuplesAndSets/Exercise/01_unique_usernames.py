# Read input for N lines
collection = set([input() for x in range(int(input()))])

# Unpack the collection separated with new lines
print(*collection, sep='\n')
