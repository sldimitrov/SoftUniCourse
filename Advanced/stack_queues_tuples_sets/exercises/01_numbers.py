first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

for i in range(int(input())):
    action, number, *data = input().split()
    command = action + ' ' + number

    if command == "Add First":
        [first_set.add(int(x)) for x in data]
    elif command == "Add Second":
        [second_set.add(int(x)) for x in data]
    elif command == "Remove First":
        [first_set.discard(int(x)) for x in data]
    elif command == "Remove Second":
        [second_set.discard(int(x)) for x in data]
    elif command == "Check Subset":
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')
