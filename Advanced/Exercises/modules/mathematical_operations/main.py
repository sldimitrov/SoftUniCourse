from core import divide, multiply, subtract, addition, raising

# Read User input
sequence = input()

# Initialise a mapper dictionary
sign_mapper = {
    "/": divide,
    "*": multiply,
    "-": subtract,
    "+": addition,
    "^": raising,
}

# Unpack the sequence elements
num_1, sign, num_2 = sequence.split()

# Try to convert the numbers into integer

num_1, num_2 = float(num_1), float(num_2)


print(sign_mapper[sign](num_1, num_2) if sign_mapper.get(sign) else "Invalid operator")