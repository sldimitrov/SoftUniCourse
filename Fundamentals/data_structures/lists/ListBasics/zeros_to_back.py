# Read User input
single_strings_list = input().split(',')
single_integers_list = []
for string in single_strings_list:
    single_integers_list.append(int(string))
for integer in single_integers_list:
    if integer == 0:
        single_integers_list.remove(0)
        single_integers_list.append(0)
print(single_integers_list)
# Logic

# Print User output