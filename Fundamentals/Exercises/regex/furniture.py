import re


# Initialise lists to store data
furniture_list = []
total_cost = 0
# Regular expression
regex = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
command = input()
while command != 'Purchase':
    match = re.search(regex, command)
    if match:
        item_name, price, quantity = match.groups()
        furniture_list.append(item_name)
        total_cost += float(price) * int(quantity)
    command = input()

# Print User output
print('Bought furniture:')
for furniture in furniture_list:
    print(furniture)
print(f'Total money spend: {total_cost:.2f}')
