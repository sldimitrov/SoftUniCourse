# Read User input
events = input().split('|')
total_energy = 100
total_coins = 100
is_shop_open = True
for event in events:
    event_items = event.split('-')
    type_of_event = event_items[0]
    event_value = int(event_items[1])
# Logic
    if type_of_event == 'rest':
        current_energy = total_energy
        current_energy += event_value
        if current_energy >= 100:
            current_energy = 100
        gained_energy = current_energy - total_energy
        print(f'You gained {gained_energy} energy.')
        total_energy = current_energy
        print(f'Current energy: {current_energy}.')
    elif type_of_event == 'order':
        if total_energy >= 30:
            total_energy -= 30
            total_coins += event_value
            print(f'You earned {event_value} coins.')
        else:
            total_energy += 50
            print('You had to rest!')
    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f'You bought {type_of_event}.')
        else:
            print(f'Closed! Cannot afford {type_of_event}.')
            is_shop_open = False
            break

if is_shop_open:
    print('Day completed!')
    print(f'Coins: {total_coins}')
    print(f'Energy: {total_energy}')
# Print User output