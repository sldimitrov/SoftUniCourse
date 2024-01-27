# Define a recursive function
def recursive_power(number, power):

    # base case / break cond.
    if power == 1:
        return number

    # recursive case / the func. call itself
    return number * recursive_power(number, power - 1)


# Call the function
print(recursive_power(2, 10))
