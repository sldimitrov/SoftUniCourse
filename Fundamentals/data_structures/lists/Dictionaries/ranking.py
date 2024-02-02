courses = {}
users_memory = {}

while True:
    command = input()
    if command == 'end of contests':
        break
    contest, password = command.split(':')
    courses[contest] = password


while True:
    is_valid = True

    command = input()
    if command == 'end of submissions':
        break

    contest, password, username, points = command.split('=>')
    points = int(points)
    if contest not in courses.keys():
        is_valid = False
    elif courses[contest] != password:
        is_valid = False
    else:   # Valid contest and password
        if username not in users_memory:
            users_memory[username] = {}
        users_memory[username] = {'contest': contest,
                                  'points': 0}

        if users_memory[username]['points'] < points:
            users_memory[username]['points'] = points

# Output #1
most_user_points = 0
most_valuable_user = ''

user_points = 0
for name in users_memory.keys():
    for key in users_memory[name].keys():
        if key == 'points':
            user_points += users_memory[name][key]
            if user_points > most_user_points:
                most_user_points = user_points
                most_valuable_user = name
print(f'Best candidate is {most_valuable_user} with total '
      f'{most_user_points} points.')

