mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Make the matrix flat
flat_list = [item for sublist in mat for item in sublist]

# Print out
print(flat_list)
print(len(flat_list))
