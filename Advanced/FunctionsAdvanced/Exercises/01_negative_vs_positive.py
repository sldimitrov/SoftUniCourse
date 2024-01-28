# Define a function
def print_numbers(nums):
    # Sum the numbers from the list
    positive_numbers = sum(x for x in nums if x > 0)
    negative_numbers = sum(x for x in nums if x < 0)

    # Print to the User
    print(negative_numbers)
    print(positive_numbers)

    # Check which absolute value is greater
    if positive_numbers > abs(negative_numbers):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


# Read the input
numbers = [int(x) for x in input().split()]
print_numbers(numbers)
