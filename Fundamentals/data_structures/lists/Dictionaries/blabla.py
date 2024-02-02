items_quantity = {}
items_price = {}
product = input().split()
while len(product) != 1:
    product_name = product[0]
    product_price = float(product[1])
    product_quantity = int(product[2])
    if product_name not in items_quantity:
        items_quantity[product_name] = product_quantity
        items_price[product_name] = product_price
    else:
        items_quantity[product_name] += product_quantity

    if items_price[product_name] != product_price:
        items_price[product_name] = product_price

    product = input().split()

for product in items_quantity.keys():
    total_price = items_quantity[product] * items_price[product]
    print(f"{product} -> {total_price :.2f}")
