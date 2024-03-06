import re

text = 'Python is fun.'


starts_pattern = '^Python'
result = re.findall(starts_pattern, text)
print(result)

ends_pattern = 'fun\.$'
result = re.findall(ends_pattern, text)
print(result)