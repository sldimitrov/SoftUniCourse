# Define the function
def data_types(type_of_object: str, object_value: str):
    if type_of_object == 'int':
        result = int(object_value) * 2
        return result
    elif type_of_object == 'real':
        result = int(object_value) * 1.5
        return f'{result:.2f}'
    elif type_of_object == 'string':
        result = f'${object_value}$'
    else:
        print("Invalid data")
    return result


# Read User input
type_of_string = input()
the_string = input()

# Print
print(data_types(type_of_string, the_string))