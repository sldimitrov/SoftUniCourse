# Define a to-do-list function
def to_do_list():
    todo_list = []

    while True:
        note = input()
        if note == 'End':
            break

        todo_list.append(note)

    sorted_notes = sorted(todo_list, key=lambda x: int(x.split("-")[0]))
    return [note.split("-")[1] for note in sorted_notes]

result = to_do_list()
print(result)

