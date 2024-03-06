# Read User input
stops = input()

# Logic
command = input()
while command != 'Travel':  # Manipulate the string
    command = command.split(':')
    action = command[0]

    if action == 'Add Stop':
        index, string = int(command[1]), command[2]
        if index in range(len(stops)):
            stops = stops[:index] + string + stops[index:]

    elif action == 'Remove Stop':
        start_index, end_index = int(command[1]), int(command[2])
        if start_index in range(len(stops)) and end_index in range(len(stops)):
            stops = stops[:start_index] + stops[end_index + 1:]

    elif action == 'Switch':
        old_string, new_string = command[1], command[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
    print(stops)
    command = input()

print(f"Ready for world tour! Planned stops: {''.join(stops)}")
