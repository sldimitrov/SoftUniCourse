import re


# Read User input
numbers = input()
# Regex about specific sequence of symbols.
regex_template = r'\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b'
# Find something specific in the string above.
matches = re.findall(regex_template, numbers)

# Print User output
print(', '.join(matches))
