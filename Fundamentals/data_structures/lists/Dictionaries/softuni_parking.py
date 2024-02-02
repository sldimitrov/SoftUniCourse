parking_users_info = {}
number_of_commands = int(input())
counter = 0
# this condition limit the number of commands
while counter < number_of_commands:
    command = input()
    if 'unregister' in command:
        command, username = command.split()
        # if person car is in the garage
        if username in parking_users_info.keys():
            print(f"{username} unregistered successfully")
            parking_users_info.pop(username)
        else:
            # if not in the garage - ERROR
            print(f"ERROR: user {username} not found")

    else:   # register condition
        command, username, plate_num = command.split()
        # if person is already register - ERROR
        if username in parking_users_info.keys():
            print(f"ERROR: already registered with plate number {plate_num}")
        else:
            # register
            parking_users_info[username] = [plate_num]
            print(f"{username} registered {plate_num} successfully")
    # increase the counter
    counter += 1

# Print all the users and car's plate numbers
for key, value in parking_users_info.items():
    print(f"{key} => {''.join(value)}")