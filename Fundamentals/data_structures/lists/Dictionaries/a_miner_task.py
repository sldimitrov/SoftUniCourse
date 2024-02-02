resources = {}
last_command = ''
counter = 1
command = input()

while command != 'stop':
    if counter % 2 != 0:
        if command not in resources.keys():
            resources[command] = 0

    else:
        quantity = int(command)
        resources[last_command] += quantity
    counter += 1
    last_command = command

    command = input()

# Print the output
for key, value in resources.items():
    print(f'{key} -> {value}')