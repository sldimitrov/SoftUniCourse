# Define a function
def grocery_store(**products):
    products = sorted(products.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0]))
    return '\n'.join(f"{p}: {q}" for p, q in products)


# Test Code
print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))