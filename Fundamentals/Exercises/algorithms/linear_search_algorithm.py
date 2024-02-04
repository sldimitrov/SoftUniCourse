# Def Linear Searching Function
def linear_searching(your_list, element):
    for i in range(len(my_list)):
        if your_list[i] == element:
            result = element
            return i
    return -1

# Read Input
my_list = [int(x) for x in input().split(',')]
target = -5

# Call the function
result = linear_searching(my_list, target)

# Print function return
print(result)