# Define a function
def rounding(numbers: list):
    """
     This function rounds all the given numbers
          from a
     :parameter: list

     :returns: list with rounded numbers
    """
    list_out = []
    for num in numbers:
        number = round(float(num))
        list_out.append(number)
    return list_out


# Read User input
list_with_numbers = input().split()

# Calls the func and print its result
print(rounding(list_with_numbers))