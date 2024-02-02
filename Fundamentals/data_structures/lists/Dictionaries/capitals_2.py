countries = [x for x in input().split(", ")]
cities = [s for s in input().split(", ")]
some_dict = dict(zip(countries, cities))
for key, value in some_dict.items():
    print(f"{key} -> {value}")