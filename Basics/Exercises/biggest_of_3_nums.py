# Read User input
n1 = int(input())
n2 = int(input())
n3 = int(input())
# Logic
if n1 > n2:
    if n1 > n3:
        print(n1)
    else:
        print(n2)
else:
    if n2 < n3:
        print(n3)
    else:
        print(n2)

# Print User output
