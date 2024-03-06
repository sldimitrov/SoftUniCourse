groceries_list = input().split("!")

command = input()
while True:
    if command == 'Go Shopping!':
        break
    command_parts = command.split()
    action = command_parts[0]

    if action == 'Urgent':
        item = command_parts[1]

        if item not in groceries_list:
            groceries_list.insert(0, item)

    elif action == 'Unnecessary':
        item = command_parts[1]
        if item in groceries_list:
            groceries_list.remove(item)

    elif action == 'Correct':
        old_item = command_parts[1]
        new_item = command_parts[2]
        if old_item in groceries_list:
            index = groceries_list.index(old_item)
            groceries_list[index] = new_item

    elif action == 'Rearrange':
        item = command_parts[1]
        if item in groceries_list:
            groceries_list.remove(item)
            groceries_list.append(item)

    command = input()

print(', '.join(groceries_list))