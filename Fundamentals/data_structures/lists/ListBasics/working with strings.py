num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in range(6, len(num_list)):
    num_list.remove(min(num_list))

list_with_strings = str(number_list)

for number in range(4, len(number_list)):
    number_list.remove(max(number_list))
print(number_list, num_list, end=' ')