# Define a function
def sorting_cheeses(**kwargs) -> str:
    formatted_result = ''

    sorted_dictionary = sorted(
        kwargs.items(), key=lambda kvp: (len(kvp[1]), (kvp[0], reversed))
    )

    for kind, values in sorted(sorted_dictionary, reverse=True):
        formatted_result += f"{kind}\n"
        for value in values:
            formatted_result += f"{value}\n"

    return formatted_result


# Test cases
print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
