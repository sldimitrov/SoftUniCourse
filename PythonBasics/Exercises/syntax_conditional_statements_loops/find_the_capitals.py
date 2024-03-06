# Read User input
input_string = input("")
# Logic
capital_indices = [index for index, char in enumerate(input_string) if char.isupper()]
# Print User output
print(capital_indices)