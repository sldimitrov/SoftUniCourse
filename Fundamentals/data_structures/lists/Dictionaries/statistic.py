command = input()

products_in_stock = {}

while command != 'statistics':
    key, value = command.split()
    value = int(value)
    if key in products_in_stock:
        products_in_stock[key] += value
    else:
        products_in_stock[key] = value
    command = input()

print('Products in stock:')
for p in products_in_stock:
    print(f'- {p} {products_in_stock[p]}')
print(f'Total Products: {len(products_in_stock)}')
print(f'Total Quantity: {sum(products_in_stock.values())}')