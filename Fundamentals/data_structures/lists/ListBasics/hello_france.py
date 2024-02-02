# Read User input
pieces = input().split('|')
budget = int(input())
train_ticket = 150
values_list = []
profit_sum = 0
total_sum = 0
# Logic
for piece in pieces:
    args = piece.split('->')
    item_type = args[0]
    value_of_the_item = float(args[1])
    is_money_enough = False

    # If I can't buy - CONTINUE
    if budget < value_of_the_item:
        continue

    if item_type == 'Clothes' and value_of_the_item < 50:
        budget -= value_of_the_item
    elif item_type == 'Shoes' and value_of_the_item < 35:
        budget -= value_of_the_item
    elif item_type == 'Accessories' and value_of_the_item < 20.5:
        budget -= value_of_the_item
    else:
        continue
    # Adding the sells in total sum
    new_value = value_of_the_item * 1.4
    total_sum += new_value
    print(f'{new_value:.2f}',end=' ')
    # Calculating the profit for each in a sum
    profit = new_value - value_of_the_item
    profit_sum += profit

total_sum += budget
print()
print(f'Profit: {profit_sum:.2f}')
if total_sum > 150:
    print('Hello, France!')
else:
    print('Not enough money.')
# Print User ouput