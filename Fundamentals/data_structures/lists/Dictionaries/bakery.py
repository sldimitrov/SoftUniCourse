# Read User input and split by space
data_container = input().split()

# Initialise the dict
initialised_dictionary = {}

# Initialise a for loop to iterate through the data
for i in range(0, len(data_container), 2):
    food_key = data_container[i]
    quantities_value = int(data_container[i + 1])
    # Adding the pair of key and value to the dict
    initialised_dictionary[food_key] = quantities_value

# Print User output
print(initialised_dictionary)