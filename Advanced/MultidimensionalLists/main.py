# One way to initialize a matrix

# matrix = []
# for i in range(3):
#     matrix.append([])
#     for j in range(1, 4):
#         matrix[i].append(j)
#
# print(matrix)


# # Another one
# total_sum = 0
# matrix = []
# for i in range(3):
#     sub_list = []
#     for j in range(1, 4):
#         sub_list.append(j)
#     matrix.append(sub_list)
#     total_sum += sum(sub_list)  # sum the elements of each list
#
# print(total_sum)
# print(matrix)


# the length of each list
matrix = [[1, 2, 3], [4, 5, 6], [8, 9]]
for i in range(len(matrix)):
    print(f'list: {matrix[i]}')
    print(f'length: {len(matrix[i])}')
