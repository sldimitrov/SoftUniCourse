def sorting_cheeses(**kwargs):
    formatted_result = ''

    sorted_result = sorted(
                    kwargs.items(),
                    key=lambda kvp: (-len(kvp[1]), kvp[0])
                    )

    for kind, values in sorted_result:
        formatted_result += f"{kind}\n"
        for value in sorted(values, reverse=True):
            formatted_result += f"{value}\n"

    return formatted_result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
