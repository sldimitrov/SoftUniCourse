string = input()
herd = string.split(', ')
if herd[-1] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    herd_length = len(herd)
    position_of_wolf = herd.index('wolf')
    sheep_in_danger = (herd_length - 1) - position_of_wolf
    print(f'Oi! Sheep number {sheep_in_danger}! You are about to be eaten by a wolf!')