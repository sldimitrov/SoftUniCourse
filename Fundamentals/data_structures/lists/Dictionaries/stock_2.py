data = input().split()

dictionary = {}

for i in range(0, len(data), 2):
    key = data[i]
    value = data[i+1]
    dictionary[key] = int(value)

searched_products = input().split()
for product in searched_products:
    if product in dictionary:
        print(f"We have {dictionary[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")