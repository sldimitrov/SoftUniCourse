def sort_names():
    names_list = [name for name in input().split("", )]

    return sorted(names_list, key=lambda name: (-len(name), name))

print(sort_names())