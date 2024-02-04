# Define a function
def perfect_number(positive_integer: int):
    list_of_dividers = []
    for i in range(1, positive_integer):
        if positive_integer % i == 0:
            list_of_dividers.append(int(i))
    if sum(list_of_dividers) == positive_integer:
        return 'We have a perfect number!'
    else:
        return 'It\'s not so perfect.'


# Read User input
number = int(input())
sum_list = 0

# Print the return of the function
print(perfect_number(number))

