import os

while True:

    command, *content_info = input().split('-')

    if command == 'End':
        break

    if command == 'Create':
        file_name = content_info
        open(f"resources/{file_name}", "w")

    elif command == 'Add':
        file_name, content = content_info
        with open(f"resources/{file_name}", "a") as file:
            file.write(f"{content}\n")

    elif command == 'Replace':
        file_name, old_string, new_string = content_info
        try:
            with open(f"resources/{file_name}", "r+") as file:
                text = file.read()
                text = text.replace(old_string, new_string)

                file.seek(0)
                file.write(text)
                file.truncate()

        except FileNotFoundError:
            print("An error occurred")

    elif command == 'Delete':
        file_name = content_info
        try:
            os.remove(f"resources/{file_name}")
        except FileNotFoundError:
            print("An error occurred")
