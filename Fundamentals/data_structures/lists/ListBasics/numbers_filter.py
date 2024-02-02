# Read User input
n = int(input())
# Logic
number_list = []
for i in range(n):
    number = int(input())
    number_list.append(number)
command = input()
special_list = []

if command == 'even':
    for num in number_list:
        if num % 2 == 0:
            special_list.append(num)

elif command == 'odd':
    for num in number_list:
        if num % 2 != 0:
            special_list.append(num)

elif command == 'negative':
    for num in number_list:
        if num < 0:
            special_list.append(num)

elif command == 'positive':
    for num in number_list:
        if num >= 0:
            special_list.append(num)
print(special_list)
# Print User output