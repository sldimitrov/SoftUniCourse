
def shopping_cart(*kitchen_list) -> str:
    # Initialise a dictionary to store meals
    meal_products = {}

    # Iterate through the list of foods
    for line in kitchen_list:
        if line == "Stop":  # break condition
            break
        # Extract the meal and the given meal
        meal, product = line

        if meal == "Soup":
            if meal not in meal_products:
                meal_products[meal] = []
            if len(meal_products[meal]) < 3:
                meal_products[meal].append(product)

        if meal == "Pizza":
            if meal not in meal_products:
                meal_products[meal] = []
            if len(meal_products[meal]) < 4:
                meal_products[meal].append(product)
        if meal == "Dessert":
            if meal not in meal_products:
                meal_products[meal] = []
            if len(meal_products[meal]) < 2:
                meal_products[meal].append(product)

    result = []

    if meal_products:
        for meal in sorted(meal_products.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
            meal_name, product_required = meal
            result.append(f"{meal_name}:")
            for product in sorted(product_required, key=lambda x: x[0]):
                result.append(f" - {product}")

    else:
        result.append("No products in the cart!")

    return '\n'.join(result)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

