# Define a function
def check_for_positive_numbers(some_list: list)-> str:
    print(f"Positive: {', '.join([number for number in numbers if int(number) >= 0])}")


def check_for_negative_numbers(some_list: list)-> str:
    print(f"Negative: {', '.join([number for number in numbers if int(number) < 0])}")


def check_for_even_numbers(some_list: list)-> str:
    print(f"Even: {', '.join([number for number in numbers if int(number) % 2 == 0])}")


def check_for_odd_numbers(some_list: list)-> str:
    print(f"Odd: {', '.join([number for number in numbers if int(number) % 2 != 0])}")


# Read User input
numbers = input().split(", ")
check_for_positive_numbers(numbers)
check_for_negative_numbers(numbers)
check_for_even_numbers(numbers)
check_for_odd_numbers(numbers)