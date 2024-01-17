def binarySearch(lst, x):
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