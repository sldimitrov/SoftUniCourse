import re

# Initialise regular expression
p = re.compile(r"^[0-9]+$", re.S)

num = "123"
snum = "s123"

if p.search(num):
    print('Number')
else:
    print('String')

if p.search(snum):
    print('Number')
else:
    print('String')