# Define a function
def min_max_sum(string_list: list):
    list_with_integers = []
    for element in string_list:
        list_with_integers.append(int(element))
    min_value = min(list_with_integers)
    max_value = max(list_with_integers)
    sum_value = sum(list_with_integers)
    return min_value, max_value, sum_value


# Read User input
input_list = input().split()
minimum, maximum, sum_t = min_max_sum(input_list)

# Print result from the function
print(f'The minimum number is {minimum}')
print(f'The maximum number is {maximum}')
print(f'The sum number is: {sum_t}')