# Read User input
sequence_of_numbers = [int(x) for x in input().split()]
counter = 0
greater_list = []
average = sum(sequence_of_numbers) // len(sequence_of_numbers)
for num in range(len(sequence_of_numbers)):
    if counter >= 5:
        break
    max_number = max(sequence_of_numbers)
    if max_number > average:
        greater_list.append(max_number)
        sequence_of_numbers.remove(max_number)
    else:
        break
    counter += 1

if greater_list:
    for each in greater_list:
        print(each,end=' ')
else:
    print("No")
