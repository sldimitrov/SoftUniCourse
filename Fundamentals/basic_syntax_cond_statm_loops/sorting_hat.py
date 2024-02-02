# Read User input
are_sorted_successfully = True
# Logic
command = input()
while command != 'Welcome!':
    if command == 'Voldemort':
        are_sorted_successfully = False
        print('You must not speak of that name!')
        break
    length_of_name = 0
    name = command
    for char in name:
        length_of_name += 1
    if length_of_name < 5:
        print(f'{name} goes to Gryffindor.')
    elif length_of_name == 5:
        print(f'{name} goes to Slytherin.')
    elif length_of_name == 6:
        print(f'{name} goes to Ravenclaw.')
    elif length_of_name > 6:
        print(f'{name} goes to Hufflepuff.')
    command = input()
if are_sorted_successfully:
    print('Welcome to Hogwarts.')
# Print User output
