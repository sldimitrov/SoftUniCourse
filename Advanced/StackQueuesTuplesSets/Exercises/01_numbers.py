# Read User input
first_set = set([int(x) for x in input().split()])
second_set = set([int(x) for x in input().split()])

# Logic
for i in range(int(input())):  # n times
    action, sequence, *numbers = input().split()
    # concatenate sequence and action together
    command = action + ' ' + sequence

    if command == "Add First":
        for el in numbers:
            el = int(el)
            first_set.add(el)
    elif command == "Add Second":
        for el in numbers:
            el = int(el)
            second_set.add(el)
    elif command == "Remove First":
        for el in numbers:
            el = int(el)
            if el in first_set:
                first_set.remove(el)
    elif command == "Remove Second":
        for el in numbers:
            el = int(el)
            if el in second_set:
                second_set.remove(el)
    elif command == "Check Subset":  # Example - if a contains b print True
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

# Print User output
print(", ".join(sorted([str(x) for x in first_set])))
print(", ".join(sorted([str(x) for x in second_set])))
