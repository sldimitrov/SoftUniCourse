# Initialise a While loop
counter = 0
miner_dictionary = {}
last_command = ''

while True:
    command = input()
    # increment by 1 with every input
    counter += 1

    # implement ending condition
    if command == 'stop':
        break

    if counter % 2 != 0:
        # if resource is not implemented as a key in the dict:
        if command not in miner_dictionary.keys():
            # create a new key with value 0
            miner_dictionary[command] = 0

    else:
        # if counter is even
        # adding quantity to the given resource
        miner_dictionary[last_command] += int(command)
    # save the name of the resource
    last_command = command

# Print the output
for key, value in miner_dictionary.items():
    print(f'{key} -> {value}')
