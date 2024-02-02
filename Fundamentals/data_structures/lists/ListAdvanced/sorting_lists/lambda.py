some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter always returns an object
returned_object = filter(lambda x: x % 2 == 1, some_list)

# We should use list() to access the values
print(list(returned_object))
