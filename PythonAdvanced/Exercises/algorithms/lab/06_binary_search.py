def binary_search(collection: list, searched_el: int):
    left_idx = 0
    right_idx = len(collection) - 1

    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        current_element = collection[mid_idx]

        if current_element == searched_el:
            return mid_idx
        elif current_element < searched_el:
            left_idx = mid_idx + 1
        elif current_element > searched_el:
            right_idx = mid_idx - 1

    return -1


some_list = [int(x) for x in input().split()]
element = int(input())

print(binary_search(some_list, element))