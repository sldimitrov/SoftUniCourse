import os
import re


def save_extensions(dir_name, string_to_replace, string_to_replace_with):
    result = []

    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)

        if os.path.isfile(file):
            if string_to_replace in file:
                new_name = filename.replace(string_to_replace, string_to_replace_with)
                new_file = "/".join(re.split(r"[\\/]", file)[:-1]) + "/" + new_name
                os.rename(file, new_file)

        elif os.path.isdir(file):
            save_extensions(file, string_to_replace, string_to_replace_with)

    return result


directory = input("Enter a directory: ")
str_to_replace = input("Enter a string to replace: ")
str_to_replace_with = input("Enter a string to replace with: ")

try:
    save_extensions(directory, str_to_replace, str_to_replace_with)
except FileNotFoundError:
    print("Directory not found!")

