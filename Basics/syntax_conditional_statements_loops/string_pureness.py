# Read User input
counter = int(input())
# Logic
for i in range(counter):
    string = input()
    is_pure = True
    for index in string:
        if index == ',' or index == '.' or index == '_':
            is_pure = False
            break
    if not is_pure:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")
# Print User input