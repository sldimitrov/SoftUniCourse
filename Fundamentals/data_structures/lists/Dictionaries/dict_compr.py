
# Initialise a list
nums = [1, 2, 3]

# Iterate through the element of the list
# makes a new dict with the nums as keys and
# their powers as values
cubes = {num: num ** 3 for num in nums}

# Print the new dict
print(cubes)