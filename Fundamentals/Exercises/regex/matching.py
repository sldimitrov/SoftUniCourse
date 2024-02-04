import re


regex = r"\b[A-Z][a-z]{1,}\s[A-Z][a-z]{1,}\b"

text = input()
match = re.findall(regex, text)
print(' '.join(match))