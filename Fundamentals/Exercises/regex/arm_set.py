import re

text = """
I am bord 30-Dec-1994.
My father is born 9-Jul-1995.
"""
pattern = r'\b\d{1,2}-[A-Z][a-z]{2}-\d{4}\b'
result = re.findall(pattern, text)

for match in result:
    print(''.join(match))