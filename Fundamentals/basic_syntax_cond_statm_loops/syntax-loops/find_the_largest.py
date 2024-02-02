number = input()

digits = list(number)

digits.sort(reverse=True)

digits_as_str = ''.join(digits)

output = int(digits_as_str)
print(output)