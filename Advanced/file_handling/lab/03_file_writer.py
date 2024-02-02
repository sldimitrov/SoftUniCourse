import os

# Initialise the name of the file
file = "my_first_file.txt"
# and the text we need to write in it
content = "I just created my first file!"

# Then choose the exact path for the initialisation
path = os.path.join("resources", file)

# Open the file
with open(path, "w") as f:  # close the file automatically
    # write content in it
    f.write(content)

