from constants import sign_mapper

# Read User input
sequence = input()

# Unpack the sequence elements
num_1, sign, num_2 = sequence.split()

# Try to convert the strings into float values
num_1, num_2 = float(num_1), float(num_2)

# Find the result of the math sequence
result = (sign_mapper[sign](num_1, num_2) if sign_mapper.get(sign) else "Invalid operator")

# Print Use output
print(f"{result}")
