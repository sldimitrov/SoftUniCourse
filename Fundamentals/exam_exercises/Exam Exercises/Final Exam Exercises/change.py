# Read User input
string = input()

# Logic
while True:
    command = input()
    if command == 'Done':
        break
    command = command.split()
    action = command[0]

    if action == 'Change':
        char, replacement = command[1], command[2]
        if char in string:
            string = string.replace(char, replacement)
            print(string)

    elif action == 'Includes':
        substring = command[1]
        if substring in string:
            print('True')
        else:
            print('False')

    elif action == 'End':
        substring = command[1]
        length = len(substring)
        if string[-length:] == substring:
            print('True')
        else:
            print('False')

    elif action == 'Uppercase':
        string = string.upper()
        print(string)

    elif action == 'FindIndex':
        char = command[1]
        index = string.index(char)
        print(index)

    elif action == 'Cut':
        start_index, count = command[1], command[2]
        start_index, count = int(start_index), int(count)

        remove = string[start_index:start_index+count]
        print(remove)
        string = string[:start_index] + string[start_index+count:]

