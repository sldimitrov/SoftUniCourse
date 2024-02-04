# Define a function
def even_numbers(my_list):
    even_list = []
    for element in my_list:
        if int(element) % 2 == 0:
            even_list.append(int(element))
    return even_list


# Define a function
def odd_numbers(another_list):
    odd_list = []
    for element in another_list:
        if int(element) % 2 != 0:
            odd_list.append(int(element))
    return odd_list


# Read User input
test_list = input().split()

# Print the return of the function
print(even_numbers(test_list))
print(odd_numbers(test_list))
