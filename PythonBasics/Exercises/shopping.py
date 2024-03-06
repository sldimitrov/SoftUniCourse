# Read User input
budget = int(input())
payed = 0;

is_overwell = False
command = input()
# Logic
while command != 'End':
    payed += int(command)
    if payed > budget:
        is_overwell = True
        print('You went in overdraft!')
        break
    command = input()

if not is_overwell:
    print('You bought everything needed.')
# Print User output