# Initialise a dict to store the data
order_info = {}

# Initialise a While loop
while True:
    command = input()

    # break condition
    if command == "buy":
        break

    # Split by space and pass numbers into float
    name, price, quantity = command.split()
    price, quantity = float(price), float(quantity)

    if name not in order_info.keys():
        order_info[name] = [price, 0]
    order_info[name][1] += quantity
    if price != order_info[name][0]:
        order_info[name][0] = price

for key, value in order_info.items():
    total = 0
    x = 0
    counter = 0
    for v in value:
        if counter == 0:
            x = v
        else:
            total = x * v
        counter += 1
    print(f"{key} -> {total:.2f}")