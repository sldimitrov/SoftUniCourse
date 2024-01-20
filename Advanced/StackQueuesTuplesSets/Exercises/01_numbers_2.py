first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

functions = {
    "Add First": lambda x: [first_set.add(int(i)) for i in x],
    "Add Second": lambda x: [second_set.add(int(i)) for i in x],
    "Remove First": lambda x: [first_set.discard(int(i)) for i in x],
    "Remove Second": lambda x: [second_set.discard(int(i)) for i in x],
    "Check Subset": lambda x: [print(first_set.issubset(second_set) or second_set.issubset(first_set))],
}

for i in range(int(input())):
    action, number, *data = input().split()
    command = action + ' ' + number

    functions[command](data)

print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')
