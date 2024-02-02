def positive_numbers(some_list: list)-> list:
    positive_list = [x for x in numbers_list if int(x) >= 0]
    return positive_list


def negative_numbers(some_list: list)-> list:
    negative_list = [x for x in numbers_list if int(x) < 0]
    return negative_list


def even_numbers(some_list: list)-> list:
    even_list = [x for x in numbers_list if int(x) % 2 == 0]
    return even_list


def odd_numbers(some_list: list)-> list:
    odd_list = [x for x in numbers_list if int(x) % 2 != 0]
    return odd_list


# Read User input
numbers_list = input().split(", ")

# Call the functions and take the returns
positives = positive_numbers(numbers_list)
negatives = negative_numbers(numbers_list)
evens = even_numbers(numbers_list)
odds = odd_numbers(numbers_list)

# Print the list elements as int numbers
            # split by ", "
print("Positive: " + ", ".join(positives))
print("Negative: " + ", ".join(negatives))
print("Even: " + ", ".join(evens))
print("Odd: " + ", ".join(odds))