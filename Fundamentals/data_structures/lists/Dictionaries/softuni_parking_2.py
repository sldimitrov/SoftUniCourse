# Initialise a dictionary to store the data
users_info = {}
# Read User input
n = int(input())
for entry in range(n):
    command = input().split()
    if 'un' not in command[0]:  # register
        username, plate_number = command[1], command[2]
        if username not in users_info:
            users_info[username] = plate_number
            print(f"{username} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_number}")
    else:  # unregister
        username = command[1]
        if username not in users_info:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            users_info.pop(username)

for name, plate in users_info.items():
    print(f"{name} => {plate}")