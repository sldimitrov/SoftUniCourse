import re


line = input()
word = input()
pattern = fr"(?i)\b{word}\b"
result = re.findall(pattern, line)
print(len(result))
