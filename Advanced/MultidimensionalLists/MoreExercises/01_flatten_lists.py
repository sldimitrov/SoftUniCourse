# # Read data and initialise the matrix
# matrix = [[int(x) for x in i.split()] for i in input().split('|')]
#
# # Print the matrix backwards
# [print(*sub_matrix, end=' ') for sub_matrix in matrix[::-1]]


# solution 2
line = input().split('|')

sub_lists = []

for el in line[::-1]:
    sub_lists.extend(el.split())

print(*sub_lists)
