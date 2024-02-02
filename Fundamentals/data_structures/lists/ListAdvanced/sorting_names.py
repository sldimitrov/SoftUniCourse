# Initializing a list by list comprehension
def sorting_names():
    names_list = [name for name in input().split(",")]

# Sorting the list by len of the words and then by the alphabet
    return sorted(names_list, key=lambda x: (-len(x), x))


# Print the output of the function
print(sorting_names())
