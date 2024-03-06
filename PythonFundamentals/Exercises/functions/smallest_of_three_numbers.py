# Define function
def smallest_of_three(list_int: list):
    """
    Find the smallest of 3 integers within a list
    :returns int
    """
    return min(list_int)


# Read User input
first_n = int(input())
second_n = int(input())
third_n = int(input())
list_with_integers = first_n, second_n, third_n

# Print function output
print(smallest_of_three(list_with_integers))
