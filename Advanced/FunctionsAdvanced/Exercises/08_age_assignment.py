# Define a function
def age_assignment(*names, **age_data):
    result = []

    for name in names:
        for letter, age in age_data.items():
            if name.startswith(letter):
                result.append(f"{name} is {age} years old.")
                break

    return '\n'.join(result)


# Test code
print(age_assignment("Peter", "George", G=26, P=19))