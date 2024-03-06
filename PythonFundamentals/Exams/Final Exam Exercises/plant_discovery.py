
lines = int(input())

stored_info = {}
for _ in range(lines):
    plant, rarity = input().split('<->')
    if plant not in stored_info:
        stored_info[plant] = {'rarity': 0, 'rating': []}
    stored_info[plant]['rarity'] = int(rarity)

while True:
    command = input()
    if command == 'Exhibition':
        break
    command = command.split(': ')
    if command[0] == 'Rate':
        plant, rating = command[1].split(' - ')
        stored_info[plant]['rating'].append(int(rating))

    elif command[0] == 'Update':
        plant, new_rarity = command[1].split(' - ')
        stored_info[plant]['rarity'] = new_rarity

    elif command[0] == 'Reset':
        plant = command[1]
        stored_info[plant]['rating'] = [0]

print('Plants for the exhibition:')
for plant, info in stored_info.items():
    # print(info['rarity'])
    total_rate_points = 0
    for rate in info['rating']:
        total_rate_points += rate
    average = total_rate_points / len(info['rating'])
    print(f"- {plant}; Rarity: {info['rarity']}; Rating: {average:.2f}")