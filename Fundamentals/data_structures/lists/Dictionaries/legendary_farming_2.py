storage = {"shards": 0, "fragments": 0, "motes": 0}
is_obtained = False
legendary_item = ''

while not is_obtained:
    text = input().split()
    for i in range(0, len(text), 2):
        quantity = text[i]
        item = text[i + 1].lower()
        if item not in storage:
            storage[item] = 0
        storage[item] += int(quantity)
        if storage["shards"] >= 250:
            storage["shards"] -= 250
            legendary_item = "Shadowmourne"
            is_obtained = True
        elif storage["fragments"] >= 250:
            storage["fragments"] -= 250
            legendary_item = "Valanyr"
            is_obtained = True
        elif storage["motes"] >= 250:
            storage["motes"] -= 250
            legendary_item = "Dragonwrath"
            is_obtained = True
        if is_obtained:
            break

print(f"{legendary_item} obtained!")
for key, value in storage.items():
    print(f"{key}: {value}")