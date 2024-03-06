def insertion_sort(nums):
    for i in range(1, len(nums)):  # Iterate through the sequence of numbers
        key = nums[i]  # we get key because it will disappear while we iterate
        j = i - 1  # we get the last value of the sorted part

        # while not in the beginning
        # and while not access a pos where we can put the key
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]  # shift elements
            j -= 1  # move left

        nums[j+1] = key  # put the key on valid pos


# Read User input
numbers = [int(x) for x in input().split()]
# Sort the numbers
insertion_sort(numbers)
# Print User output
print(*numbers)
