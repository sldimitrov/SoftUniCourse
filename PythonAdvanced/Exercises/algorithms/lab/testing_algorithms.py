def selection_sort(numbers):
    for idx in range(len(numbers)):
        min_idx = idx
        for curr_idx in range(idx + 1, len(numbers)):
            if numbers[curr_idx] < numbers[min_idx]:
                min_idx = curr_idx

        numbers[idx], numbers[min_idx] = numbers[min_idx], numbers[idx]

    return numbers


def bubble_sort(nums):
    is_sorted = False
    i = 0

    while not is_sorted:
        is_sorted = True
        for j in range(1, len(nums)):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
                is_sorted = False

        i += 1

    return nums


# ------------------- Bubble sort ----------------------
# Read User input
collection = [int(x) for x in input().split()]

print(*bubble_sort(collection))

# ------------------- Selection sort -------------------
# Read User input
# # Read User input
# collection = [int(x) for x in input().split()]
# Call the function
# sorted_collection = selection_sort(collection)
# # Print the result
# print(*sorted_collection)
