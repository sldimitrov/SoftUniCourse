secret_message = input().split()
output_list = []


for word in secret_message:
    elements = list(map(str, word))

    # Take the ASCII representation of the number in SM
    digits = [str(x) for x in elements if x.isnumeric()]
    number = ''
    for each in digits:
        number += each
        if each in elements:
            elements.remove(each)

    # Change the first letter with the last one
    secret_symbol = chr(int(number))
    output_list.append(secret_symbol)
    for s in range(1):
        elements[0], elements[-1] = elements[-1], elements[0]

    # Form the output
    for element in elements:
        output_list.append(element)
    output_list.append(' ')

# Print the list output
for x in output_list:
    print(x,end='')


