import re


# IGNORE CASE
p = re.compile(r"^[a-z]+$", re.I)
print(f'Found' if p.search("ABC") else "Not found")
# Without
p = re.compile(r"^[a-z]+$")
print(f'Found' if p.search("ABC") else "Not found")