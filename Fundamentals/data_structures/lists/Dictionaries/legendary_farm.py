storage = {"shards": 0, "fragments": 0, "motes": 0}
is_obtained = False
legendary_item = ''

while not is_obtained:
    objects = input().split()
    for i in range(0, len(objects), 2):
        quantity = objects[i]
        material = objects[i + 1].lower()
        if material not in storage.keys():
            storage[material] = 0
        storage[material] += int(quantity)
        if storage["shards"] >= 250:
            storage["shards"] -= 250
            legendary_item = 'Shadowmourne'
            is_obtained = True
        elif storage["fragments"] >= 250:
            storage["fragments"] -= 250
            legendary_item = 'Valanyr'
            is_obtained = True
        elif storage["motes"] >= 250:
            storage["motes"] -= 250
            legendary_item = 'Dragonwrath'
            is_obtained = True
        if is_obtained:
            break

print(f'{legendary_item} obtained!')
for key, value in storage.items():
    print(f'{key}: {value}')






