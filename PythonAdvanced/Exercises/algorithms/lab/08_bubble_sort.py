# Define a function

def bubble_sort(nums):
    is_sorted = False
    i = 0

    while not is_sorted:
        is_sorted = True
        for j in range(1, len(nums)):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                is_sorted = False

        i += 1

    return nums


# Read User input
collection = [int(x) for x in input().split()]

print(*bubble_sort(collection))
