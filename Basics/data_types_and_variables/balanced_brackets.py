input_lines = int(input())

is_balance = True
position = ''

for _ in range(input_lines):
    new_line = input()

    if new_line == '(' and position == '':
        position = 'open'
    elif new_line == '(' and position != '':
        is_balance = False

    if new_line == ')' and position == 'open':
        position = ''
    elif new_line == ')' and position != 'open':
        is_balance = False

if is_balance:
    print('BALANCED')
else:
    print('UNBALANCED')