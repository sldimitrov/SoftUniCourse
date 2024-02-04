# Read User input
conceal_message = input()

# Initialise a while loop
while True:
    command = input()
    # Check if the word needs to be revealed
    if command == "Reveal":
        break
    # Split the command
    command = command.split(":|:")

    if command[0] == 'InsertSpace':
        index = int(command[1])
        conceal_message = conceal_message[:index] + ' ' + conceal_message[index:]

    elif command[0] == 'Reverse':
        substring = command[1]
        if substring in conceal_message:
            conceal_message = conceal_message.replace(substring, '')
            conceal_message += substring[::-1]
        else:
            print('error')
            continue

    elif command[0] == 'ChangeAll':
        substring, replacement = command[1], command[2]
        conceal_message = conceal_message.replace(substring, replacement)
    # Print the changed message
    print(conceal_message)

# Print User output
print(f'You have a new text message: {conceal_message}')