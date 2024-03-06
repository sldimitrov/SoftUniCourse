def search(array, ln, target):
    # Traversing the array
    for i in range(ln):
        if array[i] == target:
            return i
    return -1


a = [10, 8, 6, 4, 2]
print("The given array is ", a)

x = 6
print("Element to be searched is ", x)

length = len(a)  # length of the array

ind = search(a, length, x)
if ind == -1:
    print("Element Not Found")
else:
    print("Element is at index ", ind)
