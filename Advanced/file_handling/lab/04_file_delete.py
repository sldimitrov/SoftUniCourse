import os

# Save the name of the file
file = "numbers.txt"
# Save the path of the file
path = os.path.join("resources", file)

try:  # try to remove the file
    os.remove(path)
    print("File deleted successfully!")
except FileNotFoundError:  # if it doesn't exist
    print(f"File is already deleted!")
else:  # terminates only if the try is successful
    print("Which is going to be the next?")
finally:  # terminates in each scenario
    print("Program finished")
