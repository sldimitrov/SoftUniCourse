shopping_list = {
    'foods': {'nuts': 'almonds'},
    'drinks': {'soft': 'lemonade', 'wine': 'merlot'}
}

for key, value in shopping_list.items():
    for nested_key, nested_value in value.items():
        print(f'{nested_value} bought')
        # change the value of the nested key to|
        shopping_list[key][nested_key] = 'bought'

print(shopping_list)
