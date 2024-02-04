# Initialise a dictionary to store the data
data = {}

# Save the given data
n = int(input())
for _ in range(n):
    plant, rarity = input().split('<->')
    if plant not in data.keys():
        data[plant] = {'rarity': 0, 'rating': []}
    data[plant]['rarity'] = rarity

# Initialise a while loop
while True:
    command = input().split(': ')
    if command[0] == 'Exhibition':
        break
    action = command[0]

    if action == 'Rate':
        plant, rating = command[1].split(' - ')
        if plant in data.keys():
            data[plant]['rating'].append(int(rating))
        else:
            print('error')

    elif action == 'Update':
        plant, new_rarity = command[1].split(' - ')
        if plant in data.keys():
            data[plant]['rarity'] = int(new_rarity)
        else:
            print('error')

    elif action == 'Reset':
        plant = command[1]
        if plant in data.keys():
            data[plant]['rating'] = []
        else:
            print('error')

print(f'Plants for the exhibition:')
for plant, info in data.items():
    average = 0
    if info['rating']:
        for num in info['rating']:
            average += int(num)
        average = average / len(info['rating'])
    print(f"- {plant}; Rarity: {info['rarity']}; Rating: {average:.2f}")



