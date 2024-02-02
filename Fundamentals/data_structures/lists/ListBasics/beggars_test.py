# Read User input
string_list = input().split(', ')
number_of_beggars = int(input())
list_with_integers = []
for current_string in string_list:
    list_with_integers.append(int(current_string))
total_sum = []
start_index = 0
while start_index < number_of_beggars:
    current_beggar_sum = 0
    for current_index in range(start_index, len(list_with_integers), number_of_beggars):
        current_beggar_sum += list_with_integers[current_index]
    total_sum.append(current_beggar_sum)
    start_index += 1
print(total_sum)
# Logic

# Print User output