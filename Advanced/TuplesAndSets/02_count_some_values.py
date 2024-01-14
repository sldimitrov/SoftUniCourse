# Read User input
line_of_floats = [float(x) for x in input().split()]

some_dict = {}

# Logic
for l in line_of_floats:
    if l not in some_dict:
        some_dict[l] = line_of_floats.count(l)

# Print User output
for key, value in some_dict.items():
    print(f"{key} - {value} times")