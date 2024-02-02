def add_product(items: list, products_list: dict) -> None:
    product, price, quantity = items[0], float(items[1]), int(items[2])
    if product not in products_list:
        products_list[product] = {"quantity": 0}
    products_list[product]["price"] = price
    products_list[product]["quantity"] += quantity


products = {}
get_price = lambda item: item['price'] * item['quantity']
while 1:
    items_list = input().split()
    if items_list[0] == "buy":
        break
    add_product(items_list, products)

print(*[f"{k} -> {get_price(v):.2f}" for k, v in products.items()], sep="\n")
