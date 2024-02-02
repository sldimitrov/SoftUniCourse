phonebook = {}

while True:
    command = input()
    if '-' not in command:
        n = int(command)
        break

    name, number = command.split('-')
    if name not in phonebook:
        phonebook[name] = ''
    phonebook[name] = number

for search in range(n):
    searched_name = input()
    if searched_name in phonebook:
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")