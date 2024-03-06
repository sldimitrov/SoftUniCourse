# Read User input
total_sum = 0
total_sum_with_taxes = 0
taxes = 0

# Initialize a while loop
while True:  # or while a customer type is inputted
    command = input()
    if command == 'special' or command == 'regular':
        break
    part_price = float(command)
    if part_price < 0:
        print('Invalid price!')
        continue
    total_sum += part_price
    tax = part_price * 0.2
    taxes += tax
    total_sum_with_taxes += (part_price + tax)

# Make the discount for special customers
if command == 'special':
    total_sum_with_taxes *= 0.9

# Print User output
if total_sum == 0:
    print('Invalid order!')
else:
    print(f'Congratulations you\'ve just bought a new computer!')
    print(f'Price without taxes: {total_sum:.2f}$', )
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    print(f'Total price: {total_sum_with_taxes:.2f}$' )



