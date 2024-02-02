# Read User input
counter_of_cups = 0
is_exceed = False
# Logic
event = input()
while event != "END":
    if counter_of_cups >= 5:
        is_exceed = True
    if event == 'coding':
        counter_of_cups += 1
    elif event == 'CODING':
        counter_of_cups += 2
    elif event == 'dog' or event == 'cat':
        counter_of_cups += 1
    elif event == 'DOG' or event == 'CAT':
        counter_of_cups += 2
    elif event == 'movie':
        counter_of_cups += 1
    elif event == 'MOVIE':
        counter_of_cups += 2
    event = input()

if is_exceed:
    print("You need extra sleep")
else:
    print(counter_of_cups)
# Print User output