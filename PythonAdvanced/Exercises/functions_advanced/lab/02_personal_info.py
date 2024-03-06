# Define a function
def get_info(name, age, town):
    return f"This is {name} from {town} and he is {age} years old"


# Call the function | unpack the arguments, passing them to the function
print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
