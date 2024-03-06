# Define the main function
def main_func(encmsg: str, commands: list):
    for command in commands:
        if 'Move' in command:
            number_of_letters = int(command.split('|')[-1])
            encmsg = encmsg[number_of_letters:] + encmsg[:number_of_letters]

        elif 'Insert' in command:
            command, index, value = command.split('|')
            message_list_of_letters = [x for x in encmsg]
            message_list_of_letters.insert(int(index), value)
            encmsg = ''.join(message_list_of_letters)

        elif 'ChangeAll' in command:
            command, substring, replacement = command.split('|')
            encmsg = encmsg.replace(substring, replacement)
    return encmsg


# Read User input
encrypted_message = input()
command_list = []
# Logic
while True:
    command = input()
    if command == 'Decode':
        break
    command_list.append(command)

# Print Main function output
decrypted_message = (main_func(encrypted_message, command_list))
print(f'The decrypted message is: {decrypted_message}')
