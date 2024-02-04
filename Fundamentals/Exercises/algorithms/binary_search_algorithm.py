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


nums = [int(x) for x in input().split(', ')]
target = int(input())
# Print User output
print(binary_search(nums, target))

