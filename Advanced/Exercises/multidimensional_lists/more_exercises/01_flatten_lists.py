# Read data and initialise the matrix
numbers = [string.split() for string in input().split(" ")]

# Print the matrix backwards
print(*[' '.join(sub_list) for sub_list in numbers[::-1] if sub_list])

#
# # solution 2
# line = input().split('|')
#
# sub_lists = []
#
# for el in line[::-1]:
#     sub_lists.extend(el.split())
#
# print(*sub_lists)
