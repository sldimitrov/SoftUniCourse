import re

regex = r'\d+'
command = input()
while command:
    numbers = re.findall(regex, command)
    if numbers:
        for num in numbers:
            print(num,end=' ')
    command = input()

