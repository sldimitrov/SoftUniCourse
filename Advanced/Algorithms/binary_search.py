
def binary_search(lst: list, x: str):
    low = 0
    high = len(lst)-1
    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if lst[mid] == x:
            return mid

        elif lst[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


list_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
y = 7
print(binary_search(list_of_nums, y))