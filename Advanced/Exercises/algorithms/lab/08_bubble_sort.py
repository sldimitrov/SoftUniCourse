def bubble_sort(nums):
    is_sorted = False
    iterations = 0

    while not is_sorted:
        is_sorted = True
        for idx in range(len(nums)):
            for j in range(1, len(nums) - iterations):
                i = j - 1
                if nums[j] < nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    is_sorted = False

            iterations += 1

    return nums


# Read User input
collection = [int(x) for x in input().split()]
# Call the function
sorted_collection = bubble_sort(collection)
# Print the result
print(*sorted_collection)
