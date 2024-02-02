# Read User input
text = input().split()

while True:
    command = input()
    if command == "3:1":
        break
    if "merge" in command:
        command_type, start_index, end_index = command.split()
        start_index = int(start_index)
        end_index = int(end_index)
        if start_index < 0:
            start_index = 0
        if start_index < end_index:
            if end_index >= len(text):
                end_index = len(text) - 1
            for element in range(start_index, end_index):
                text[start_index] += f"{text.pop(start_index + 1)}"

    elif "divide" in command:
        command_type, index, partitions = command.split()
        index = int(index)
        partitions = int(partitions)
        element_to_change = text.pop(index)
        len_element_to_change = len(element_to_change)
        space_between = len_element_to_change // partitions
        result = []
        for change in range(partitions - 1):
            result.append(element_to_change[:space_between])
            element_to_change = element_to_change[space_between:]
        result.append(element_to_change)
        for current_element in result[::-1]:
            text.insert(index, current_element)


print(*text)

