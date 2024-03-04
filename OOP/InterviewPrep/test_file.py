# Factorial of a number using recursion
import time


def binary_search(collection, target):
    left = 0
    right = len(collection) - 1

    while left <= right:

        mid_index = (left + right) // 2
        current_element = collection[mid_index]

        if current_element == target:
            return mid_index

        elif target < current_element:
            right = mid_index
        elif target > current_element:
            left = mid_index


numbers = [4, 6, 2, 1, 8, 12, 5, 6]
sorted_numbers = sorted(numbers)

number_to_find = int(input(f"Number to find in collection: "))

index = binary_search(sorted_numbers, number_to_find)

print(f"Index: {index}")
