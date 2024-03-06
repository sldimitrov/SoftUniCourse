# Define function
def palindrome_integers(list_example: list):
    list_with_integers = []
    output_list = []
    for number in list_example:
        is_palindrome = number[0] == number[-1]
        if is_palindrome:
            output_list.append('True')
        else:
            output_list.append('False')
    return output_list


# Read User input
list_for_checking = input().split(', ')
results = palindrome_integers(list_for_checking)

# Print User output
for result in results:
    print(result)
