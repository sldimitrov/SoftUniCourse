my_list = [1, 2, 3, 4, 5, 6]

# Escaping from index error messages with looping
#           in descending order
for index in range(len(my_list) - 1, - 1, - 1):
    if index % 2 == 0:
        my_list.pop(index)
        print(my_list)
