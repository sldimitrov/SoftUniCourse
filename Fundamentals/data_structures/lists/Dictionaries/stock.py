pairs_data = input().split()

products_dict = {}

searched_products = input().split()

for i in range(0, len(pairs_data), 2):
    key = pairs_data[i]
    value = pairs_data[i + 1]
    products_dict[key] = value

for product in searched_products:
    if product in products_dict:
        print(f'We have {products_dict[product]} of {product} left')
    else:
        print(f'Sorry, we don\'t have {product}')