password = input()

while True:
    command = input()
    if command == 'Done':
        break
    command = command.split()

    if command[0] == 'TakeOdd':
        new_password = ''
        counter = 0
        for letter in password:
            if counter % 2 != 0:
                new_password += letter
            counter += 1
        password = new_password
        print(password)
    elif command[0] == 'Cut':
        index, length = int(command[1]), int(command[2])
        password = password[:index] + password[index + length:]
        print(password)
    elif command[0] == 'Substitute':
        substring, substitute = command[1], command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print('Nothing to replace!')

print(f'Your password is: {password}')



