def main():
    sequence_of_elements = input().split()
    try_counter = 0
    while True:
        command = input()
        if command == 'end':
            print(f"Sorry you lose :(\n{' '.join(sequence_of_elements)}")
            break

        try_counter += 1
        index1, index2 = map(int, command.split())

        if is_invalid_input(index1, index2, sequence_of_elements):
            handle_invalid_input(try_counter, sequence_of_elements)
        else:
            valid_input(index1, index2, sequence_of_elements, try_counter)


def is_invalid_input(first_index: int, second_index: int, sequence: list):
    return(
        first_index == second_index
        or first_index < 0
        or second_index < 0
        or first_index >= len(sequence)
        or second_index >= len(sequence)
    )


def handle_invalid_input(counter: int, sequence: list):
    mid_index = len(sequence) // 2
    sequence.insert(mid_index, f'-{counter}a')
    sequence.insert(mid_index, f'-{counter}a')
    print("Invalid input! Adding additional elements to the board")


def valid_input(first_index: int, second_index: int, sequence: list, counter: int):
    if sequence[first_index] == sequence[second_index]:
        print(f"Congrats! You have found matching elements - {sequence[first_index]}!")
        second_el = sequence[second_index]
        sequence.pop(first_index)
        sequence.remove(second_el)
    else:
        print("Try again!")

    if not sequence:
        print(f"You have won in {counter} turns!")
        exit()


main()



