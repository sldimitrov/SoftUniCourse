import re


# Read User input
line = input()
regex = r'(\s([a-z0-9]+[a-z\-\.\,]*)@([a-z][a-z\-]+)(\.[a-z]+)+)'
emails = re.findall(regex, line)
for email in emails:
    # print
    print(email[0])