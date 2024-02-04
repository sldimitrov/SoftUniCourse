import re


# Read User input
text = input()
# Template for symbol sequence to search for
regex_pattern = r'b\[A-Z][a-z]+ [A-Z][a-z]+\b'
# Get all the repetitions from the string above
valid_names = re.findall(regex_pattern, text)

# Print the valid names separated by space
print(' '.join(valid_names))