def even_numbers_indices(integer_list):
    even_nums_indices = []
    even_nums = [num for num in integer_list if num % 2 == 0]
    for number in even_nums:
        index = integer_list.index(number)
        even_nums_indices.append(index)
    return even_nums_indices


# Read User input
some_list = list(map(int, input().split(", ")))

print(even_numbers_indices(some_list))

