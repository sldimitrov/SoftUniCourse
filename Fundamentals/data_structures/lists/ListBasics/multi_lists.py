# Read User input
factor = int(input())
count = int(input())
multiples_list = []
# Logic
for num in range(1, count + 1):
    multiples_list.append(num * factor)
print(multiples_list)
# Print User output