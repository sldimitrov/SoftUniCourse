# Define a function
def odd_and_even_sum(number: int):
    """
    This function returns the sum of all even
    and all odd digits in a given number.
    :param number: int
    :return: 2 integers
    """
    sum_of_odd = 0
    sum_of_even = 0
    for num in str(number):
        if int(num) % 2 == 0:
            sum_of_even += int(num)
        else:
            sum_of_odd += int(num)
    return sum_of_odd, sum_of_even


# Read User input
special_number = int(input())
sum_of_odd_digits, sum_of_even_digits = odd_and_even_sum(special_number)

# Print function return
print(f'Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}')
