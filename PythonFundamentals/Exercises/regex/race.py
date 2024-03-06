import re


racers = input().split(', ')
command = input()
people_names = []
people_info = {}
names_regex = r'([A-Za-z]+)'
number_regex = r'(\d)'

while command != 'end of race':
    name_of_person = ''.join(re.findall(names_regex, command))
    kilometres = re.findall(number_regex, command)
    sum = 0
    for x in kilometres:
        sum += int(x)
    if name_of_person not in people_info.keys():
        people_info[name_of_person] = sum
    else:
        people_info[name_of_person] += sum
    command = input()

top_value = 0
first_person = ''
second_value = 0
second_person = ''
third_value = 0
third_person = ''

for key, value in people_info.items():
    if key in racers:
        if value > top_value:
            first_person = key
            top_value = value
        elif value > second_value:
            second_person = key
            second_value = value
        elif value > third_value:
            third_person = key
            third_value = value

print(f'1st place: {first_person}')
print(f'2nd place: {second_person}')
print(f'3rd place: {third_person}')
