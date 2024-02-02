# Read User input
n = int(input())
first_list = []
second_list = []
count_of_positives = 0
sum_of_negatives = 0
# Logic
for i in range(n):
    number = int(input())
    if number >= 0:
        count_of_positives += 1
        first_list.append(number)
    else:
        sum_of_negatives += number
        second_list.append(number)

print(first_list)
print(second_list)
print(f'Count of positives: {count_of_positives}')
print(f'Sum of negatives: {sum_of_negatives}')
# Print User output