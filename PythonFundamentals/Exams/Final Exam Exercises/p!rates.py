cities = {}

# Adding settlements

while True:
    command = input()

    if command == 'Sail':
        break

    command = command.split('||')
    city, population, gold = command[0], int(command[1]), int(command[2])
    if city not in cities.keys():
        cities[city] = {"population": 0, "gold": 0}
    cities[city]["population"] += population
    cities[city]["gold"] += gold

while True:
    command = input()
    if command == 'End':
        break

    command = command.split("=>")
    if command[0] == 'Plunder':
        town, people, gold = command[1], int(command[2]), int(command[3])
        cities[town]['population'] -= people
        cities[town]['gold'] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[town]['population'] == 0 or cities[town]['gold'] == 0:
            cities.pop(town)
            print(f"{town} has been wiped off the map!")

    elif command[0] == 'Prosper':
        town, gold = command[1], int(command[2])
        if gold < 0:
            print('Gold added cannot be a negative number!')
        else:
            cities[town]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, city_info in cities.items():
        print(f"{city} -> Population: {city_info['population']} citizens, Gold: {city_info['gold']} kg")
else:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')