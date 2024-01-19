# Read User input
first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

# Logic
for i in range(int(input())):  # n times
    action, sequence, *data = input().split()

    command = action + ' ' + sequence

    if command == "Add First":
        [first_set.add(int(el)) for el in data]
    elif command == "Add Second":
        [second_set.add(int(el)) for el in data]
    elif command == "Remove First":
        [first_set.discard(int(el)) for el in data]
    elif command == "Remove Second":
        [second_set.discard(int(el)) for el in data]
    elif command == "Check Subset":  # Example - if a contains b print True
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

# Print User output
print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")
