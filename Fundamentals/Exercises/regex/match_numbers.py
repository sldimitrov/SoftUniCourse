import re

regex = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
text = input()
matches = re.finditer(regex, text)

for match in matches:
    print(match.group(), end=' ')
