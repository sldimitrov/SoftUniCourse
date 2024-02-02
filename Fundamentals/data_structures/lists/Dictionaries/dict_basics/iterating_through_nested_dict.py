shopping_list = {
    'drink': {'juice': 'apple'},
    'eat': {'burger': 'cheeseburger', 'salad': 'cezar'}
}

for key, value in shopping_list.items():
    for nested_key, nested_value in value.items():
        print(f"{nested_value} bought")
        shopping_list[key][nested_key] = 'bought'