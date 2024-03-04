
def binary_search(nums):
    left = 0
    right = len(nums) - 1

    while left <= right:

        mid_idx = (left + right) // 2
        curr_element = nums[mid_idx]

        if curr_element == target:
            return mid_idx
        elif curr_element < target:
            left = mid_idx
        elif curr_element > target:
            right = mid_idx


numbers = [int(x) for x in input().split()]
numbers = sorted(numbers)

target = int(input())

index = binary_search(numbers)

print(f"Target index within the list: {index}")