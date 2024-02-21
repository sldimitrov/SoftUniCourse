from core import divide, multiply, subtract, addition, raising

# Read User input
sequence = input()

# Initialise a mapper dictionary
sign_mapper = {
    "/": 'divide',
    "*": 'multiply',
    "-": 'subtract',
    "+": 'addition',
    "^": 'raising',
}

# Unpack the sequence elements
num_1, sign, num_2 = sequence.split()

# Find the required function by using the mapper
required_function = sign_mapper[sign](num_1, num_2)

