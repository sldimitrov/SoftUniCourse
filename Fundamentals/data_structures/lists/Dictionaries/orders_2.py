order_data = {}

while True:
    command = input()
    if command == 'buy':
        break
    name, price, quantity = command.split()
    if name not in order_data:
        order_data[name] = {'price': 0, 'quantity': 0}
    order_data[name]['quantity'] += float(quantity)
    if order_data[name]['price'] != price:
        order_data[name]['price'] = float(price)

for product, info in order_data.items():
    print(f"{product} -> {info['price'] * info['quantity']:.2f}")
