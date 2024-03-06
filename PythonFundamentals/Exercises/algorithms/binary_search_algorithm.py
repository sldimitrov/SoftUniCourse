# Define a function
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    # initialise a while loop
    while left <= right:
        middle_index = (left + right) // 2
        middle_element = nums[middle_index]

        if middle_element == target:
            return middle_index

        if target > middle_element:
            left = middle_index + 1
        else:
            right = middle_index - 1


# Read the numbers
nums = [int(x) for x in input().split(', ')]
sorted_nums = sorted(nums)  # SORT the collection

# Read the number which index we are looking for
target = int(input())

# Save the index into a variable
index = binary_search(sorted_nums, target)  # Pass arguments to the function

# Print User output
print(index)


