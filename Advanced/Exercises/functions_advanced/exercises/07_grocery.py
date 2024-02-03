# Define a function
def grocery_store(**kwargs):
    kwargs = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0]))

    result = []

    for k, v in kwargs:
        result.append(f"{k}: {v}")

    return "\n".join(result)


# Test Code
print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))


