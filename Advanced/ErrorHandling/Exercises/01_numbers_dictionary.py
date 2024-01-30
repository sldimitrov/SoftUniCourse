numbers_dictionary = {}

# Read User input
line = input()  # Adding numbers to the dictionary
while line != "Search":
    number_as_string = line  # 'one'

    try:  # Check if a valid number is given
        number = int(input())
    except ValueError:  # Exception
        print('The variable number must be an integer!')
    else:  # if valid add - {key: value} to the dict
        numbers_dictionary[number_as_string] = number

    line = input()

# Read User input
line = input()
while line != "Remove":  # Print pairs from the dictionary
    searched = line

    try:  # Print a pair from the dictionary with key
        print(numbers_dictionary[searched])
    except KeyError:  # if the dict does not contain the key - throw an exception
        print('Number does not exist in the dictionary!')

    line = input()

# Read User input
line = input()
while line != "End":  # Remove pairs from the dictionary
    searched = line
    try:  # try to delete a pair from the dictionary
        del numbers_dictionary[searched]
    except KeyError:  # if the dict does not contain the key - throw an exception
        print('Number does not exist in the dictionary!')

    line = input()

# Print User output
print(numbers_dictionary)  # - the dictionary
