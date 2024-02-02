# Read User input
list_number = list(map(int, input().strip().split()))
count_of_number_to_remove = int(input())
for num in range(count_of_number_to_remove):
    list_number.remove(min(list_number))
print(', '.join(str(x) for x in list_number))
# Logic

# Print User output