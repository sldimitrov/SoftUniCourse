# Read User input
n = int(input())
# Logic
for number in range(1, n + 1):
    number_as_str = str(number)
    sum_of_digits = 0
    is_special = False
    for index in number_as_str:
        sum_of_digits += int(index)
        if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
            is_special = True
    print(f"{number} -> {is_special}")
# Print User output