from Advanced.Exercises.modules.fibonacci_sequence.core import create_seq, locate

sequence = []

# Read User input
command = input()
while command != "Stop":
    command_type, *args = command.split()
    if command_type == "Create":
        # Extract the sequence length from arguments
        sequence_length = int(args[1])
        # Get the sequence
        sequence = create_seq(sequence_length)
        # Print element separated by space
        print(*sequence)

    elif command_type == "Locate":
        # Extract the element from arguments
        element = int(args[0])

        # Print the index if the element is in the sequence
        print(locate(element, sequence))


    command = input()

