# Define a function
def even_numbers(sequence_of_numbers: list):
    """ 
    The function takes a list with integers as a parameter and then
    returns only the even numbers within in in another list
    :param sequence_of_numbers: list with integers
    :return: list with even numbers
    """""
    even_nums = lambda x: x % 2 == 0
    list_with_even_nums = []
    for element in sequence_of_numbers:
        list_with_even_nums = list(filter(even_nums, sequence_of_numbers))
    return list_with_even_nums


# Read User input
list_with_strings = input().split()
list_with_integers = []
for string in list_with_strings:
    list_with_integers.append(int(string))
print(even_numbers(list_with_integers))
# Print function return