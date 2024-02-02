# Read User input
n = int(input())
special = input()
my_list = []
special_list = []
# Logic
for line in range(n):
    string = input()
    my_list.append(string)
print(my_list)
for i in range(len(my_list)):
    if special in my_list[i]:
        special_list.append(my_list[i])
print(special_list)
# Print User output