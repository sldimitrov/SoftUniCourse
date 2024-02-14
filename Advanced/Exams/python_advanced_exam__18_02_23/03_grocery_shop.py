
def shop_from_grocery_list(budget, groceries_list, *items):

    for item_name, price in items:
        if item_name in groceries_list and price <= budget:
            groceries_list.remove(item_name)
            budget -= price

            if budget == 0:
                break

        elif budget < price:
            break

    result = []

    if not groceries_list:
        result.append(f"Shopping is successful. Remaining budget: {budget:.2f}.")

    else:
        result.append(f"You did not buy all the products. Missing products: {', '.join(groceries_list)}.")

    return '\n'.join(result)


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))




# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("meat", 22),
# ))
