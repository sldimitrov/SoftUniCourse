import re


# Regular Expression
regex = r"(w{3}.[A-Za-z0-9-]+(\.[a-z]+)+)"
command = input()
while True:
    # if command in not enter
    if command:
        match = re.search(regex, command)
        if match:
            print(match.group(0))
    else:
        break  # if empty string is inputted
    command = input()
