# Read User input
money_as_string = input().split(', ')
number_of_beggars = int(input())
money_as_integers = []
for current_money in money_as_string:
    money_as_integers.append(int(current_money))
total_sum = []
start_index = 0
while start_index < number_of_beggars:
    current_beggar_sum = 0
    for current_index in range(start_index, len(money_as_integers), number_of_beggars):
        current_beggar_sum += money_as_integers[current_index]
    total_sum.append(current_beggar_sum)
    start_index += 1
print(total_sum)