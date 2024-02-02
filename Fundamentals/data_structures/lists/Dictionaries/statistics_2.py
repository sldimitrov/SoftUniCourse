dictionary= {}

while True:
    command = input()
    if command == 'statistics':
        break

    key, value = command.split(': ')
    if key not in dictionary:
        dictionary[key] = 0
    dictionary[key] += int(value)

print('Products in stock:')
# Products
for key, value in dictionary.items():
    print(f'- {key}: {value}')
print(f'Total Products: {len(dictionary)}')
total_sum_of_quantities = 0
for quantity in dictionary.values():
    total_sum_of_quantities += quantity
print(f'Total Quantity: {total_sum_of_quantities}')
