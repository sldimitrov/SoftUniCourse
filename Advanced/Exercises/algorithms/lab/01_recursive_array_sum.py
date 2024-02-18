
def recursive_array_sum(array, index=0):

    # Base case
    if index == len(array) - 1:
        return array[index]

    # Call the function itself
    total_sum = array[index] + recursive_array_sum(array, index+1)

    # Start to
    return total_sum


# Read User input - call the function - print the result
print(recursive_array_sum([1, 2, 3, 4]))
