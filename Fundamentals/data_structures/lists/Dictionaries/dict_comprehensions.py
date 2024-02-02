

# Initialise a list of tuples
data = [('Peter', 22), ('Amy', 18), ('George', 35)]

# Take the keys and values from the tuples
# and represent them as a dict
dictionary = {key:value for (key,value) in data}

# Print the output
print(dictionary)