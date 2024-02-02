# Use comprehension to split the input and save
# the string within 2 lists
countries = [name for name in input().split(', ')]
capitals = [city for city in input().split(', ')]

# zip the 2  lists using countries one as keys
# and capitals as values
countries_info_dict = dict(zip(countries, capitals))

# Iterate through the dict
# print the keys and their values
for key, value in countries_info_dict.items():
    print(f'{key} -> {value}')