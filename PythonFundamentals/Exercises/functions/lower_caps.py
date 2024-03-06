# Define a function
def lower_cap(name: str) -> str:
    name = name.lower()
    return name


fist_name = input()
print(lower_cap(fist_name))
