class InvalidChoice(Exception):
    pass


class OneOrLessElements(Exception):
    pass


# Define a function for each algorithm
def selection_sort(nums):
    for idx in range(len(nums)):
        min_idx = idx

        for curr_idx in range(idx + 1, len(nums)):
            if nums[curr_idx] < nums[min_idx]:
                min_idx = curr_idx

            nums[idx], nums[min_idx] = nums[min_idx], nums[idx]

    return nums


def bubble_sort(nums):
    is_sorted = False
    i = 0

    while not is_sorted:
        is_sorted = True

        for idx in range(1, len(nums) - i):
            if nums[idx - 1] > nums[idx]:
                nums[idx], nums[idx - 1] = nums[idx - 1], nums[idx]
                is_sorted = False

        i += 1

    return nums


def insertion_sort(nums):
    # TODO: Optimate the left-moving with binary search through the list / check difference

    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key

    return nums


# Read User input
def main():
    try:
        # Read User input
        option = input("Hello user!\nThis program uses various of algorithms to sort collection of numbers.\n"
                       "'1' - Selection sort\n"
                       "'2' - Bubble sort\n"
                       "'3' - Insertion sort\n"
                       "Your choice: ")

        # Parse the input into integer values
        user_choice = int(option)

        numbers = [int(x) for x in input(f"\nEnter a collection separated with spaces e.g:  5 3 9 32 -5 1 1000\n"
                                         f"...").split()]
        if len(numbers) <= 1:
            raise OneOrLessElements

    except ValueError:
        print(f"Please input valida data next time.")
    else:

        if user_choice == 1:
            sorted_list = selection_sort(numbers)
        elif user_choice == 2:
            sorted_list = bubble_sort(numbers)
        elif user_choice == 3:
            sorted_list = insertion_sort(numbers)
        else:
            raise InvalidChoice

    print(f"Sorted collection: {', '.join([str(x) for x in sorted_list])}")
    print(f"Thank you for using this program.")


if __name__ == '__main__':
    main()