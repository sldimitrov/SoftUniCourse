# Read User input
first_sequence = input().split(", ")
second_sequence = input().split(", ")

# Initialize a list
sub_strings = []

# Checking for sub-strings of the first list within the second.
for each in first_sequence:
    for element in second_sequence:
        # if string of the first is contained in the second, append
        # it to the list
        if each in element:
            sub_strings.append(each)
            break

# Print the answer
print(sub_strings)