# Define a swat element by index function
def swap_function(index1: int, index2: int, array: list) -> list:
    array[index1], array[index2] = array[index2], array[index1]
    return array


# Define a multiplication function
def multiply_function(index1: int, index2: int, array: list) -> list:
    array[index1] = array[index1] * array[index2]
    return array


# Define a decrease number function
def decrease_function(array: list) -> list:
    index = 0
    for s in array:
        array[index] -= 1
        index += 1
    return array


# Read User input
integer_list = [int(x) for x in input().split()]
command = input()
while command != 'end':
    if 'swap' in command or 'multiply' in command:
        command_type, (first_index), second_index = command.split()
    elif command == 'decrease':
        command_type = command

    if command_type == 'swap':
        swap_function(int(first_index), int(second_index), integer_list)

    elif command_type == 'multiply':
        multiply_function(int(first_index), int(second_index), integer_list)

    elif command_type == 'decrease':
        decrease_function(integer_list)

    command = input()

# Print the main func output
for num in integer_list:
    if num != integer_list[-1]:
        print(num, end=', ')
    else:
        print(num)
