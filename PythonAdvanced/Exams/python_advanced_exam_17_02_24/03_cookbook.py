def cookbook(*meals):
    # Initialise a dictionary
    cookbook_dictionary = {}

    # Iterate over the data
    for meal in meals:
        name, home, ingredients = meal
        if home not in cookbook_dictionary:
            cookbook_dictionary[home] = []
        cookbook_dictionary[home].append([name, ingredients])

    # Sort the dictionary
    sorted_book = sorted(cookbook_dictionary.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    # Initialise a list for the return
    result = []

    # Append the output data into the list
    for cuisine, receipts_info in sorted_book:
        # Sort the receipts
        sorted_receipts = sorted(receipts_info, key=lambda kvp: kvp[0])
        result.append(f"{cuisine} cuisine contains {len(receipts_info)} recipes:")

        for meal, ingredients in sorted_receipts:
            result.append(f"  * {meal} -> Ingredients: {', '.join(ingredients)}")

    return '\n'.join(result)


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
