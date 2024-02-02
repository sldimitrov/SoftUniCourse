# Creating an empty list
my_list = []
# Logic
for x in range(3):
    data = input()
    my_list.append(data)

my_list[0], my_list[2] = my_list[2], my_list[0]

print(my_list)
# Print User output