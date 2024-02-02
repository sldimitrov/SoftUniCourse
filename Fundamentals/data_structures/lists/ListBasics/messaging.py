# Read the sequences of numbers and the string
numbers_sequence = input().split()
text = input()

# Calculate the sum of digits for each number
digit_sums = [sum(map(int, num)) for num in numbers_sequence]

# Initialize an empty message
message = ""

# Loop through the list of digit sums
for digit_sum in digit_sums:
    # Ensure the index is within the bounds of the text
    index = digit_sum % len(text)

    # Append the character at the calculated index to the message
    message += text[index]

    # Remove the character from the text
    text = text[:index] + text[index + 1:]

# Print the final message
print(message)