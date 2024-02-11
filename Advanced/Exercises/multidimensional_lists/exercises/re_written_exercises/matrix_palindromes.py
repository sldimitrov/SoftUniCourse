# Read the size of the matrix
rows, cols = [int(x) for x in input().split()]

# Save every letter from the alphabet in a list
alphabet = [chr(x) for x in range(97, 97 + 26)]

# Logic
for row in range(1, len(alphabet)):
    counter = row
    for col in range(cols):
        # Print User output - every row
        print(alphabet[row] + alphabet[counter] + alphabet[row], end=' ')
        counter += 1

    # if number of the letter in the alphabet is equal than the number of rows
    if row == rows:
        break
    print()  # print every row on a new line
