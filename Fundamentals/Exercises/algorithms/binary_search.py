
def binary_search(collection, target):
    left = 0
    right = len(collection) - 1

    while left <= right:

        mid_index = (left + right) // 2
        curr_element = collection[mid_index]

        if curr_element == target:
            return mid_index

        elif target < curr_element:
            right = mid_index
        elif target > curr_element:
            left = mid_index


# Read User input
numbers = [int(x) for x in input().split()]
numbers = sorted(numbers)  # sort the list

magic_number = int(input())

# Pass arguments into the function
index = binary_search(numbers, magic_number)

# Print User output
print(index)
