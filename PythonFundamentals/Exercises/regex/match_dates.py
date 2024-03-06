import re

data_info = input()
regex_template = r'([\d]{2})([-.\/])([A-Z][a-z]{2})\2([\d]{4})'

results = re.findall(regex_template, data_info)

for res in results:
    d = res[0]
    m = res[2]
    y = res[3]
    print(f'Day: {d}, Month: {m}, Year: {y}')
