# Define a function
def concatenate(*args, **kwargs):
    text = ''.join(args)  # concatenate all args

    for key, value in kwargs.items():
        if key in text:  # check if key is in the text
            text = text.replace(key, value)  # change it with a new value

    return text  # return the repaired text


# Test Code
print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
