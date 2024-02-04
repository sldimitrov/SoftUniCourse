import re


# Doesnt count the . as \n
p = re.compile(r'^.+$')
print(p.findall("s1\ns2\n/s3"))

# But with S flag it does
p = re.compile(r"^.+$", re.S)
print(p.findall("s1\ns2\n\s3"))
