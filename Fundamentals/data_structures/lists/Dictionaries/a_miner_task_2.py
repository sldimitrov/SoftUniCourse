miner_data = {}
counter = 1
while True:
    command = input()
    if command =='stop':
        break
    if counter % 2 != 0:
        resource = command
        if resource not in miner_data:
            miner_data[resource] = 0
    else:
        quantity = command
        miner_data[last_command] += int(quantity)

    last_command = command
    counter += 1

for key, value in miner_data.items():
    print(f"{key} -> {value}")