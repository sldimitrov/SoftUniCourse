def selection_sort(nums):
    for idx in range(len(nums)):   # iterating each element
        min_idx = idx
        for curr_idx in range(idx + 1, len(nums)):  # iterating over each element from the curr index one to the last el
            if nums[curr_idx] < nums[min_idx]:  # find the index with the lowest value
                min_idx = curr_idx

        nums[idx], nums[min_idx] = nums[min_idx], nums[idx]  # reverse the curr index with the lowest value

    return nums


# Read User input
collection = [int(x) for x in input().split()]
# Call the function
sorted_collection = selection_sort(collection)
# Print the result
print(*sorted_collection)
