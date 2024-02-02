# Read User input
numbers_list = [int(x) for x in input().split(', ')]
result = 1

# Iterate through the indexes
for i in range(len(numbers_list)):
    number = numbers_list[i]
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number

# Print User output
print(result)
