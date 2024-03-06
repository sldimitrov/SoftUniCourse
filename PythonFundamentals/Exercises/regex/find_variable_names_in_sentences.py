import re

regex_expression = r'\b_([A-Za-z0-9]+)\b'
line = input()
result = re.findall(regex_expression, line)
print(','.join(result))