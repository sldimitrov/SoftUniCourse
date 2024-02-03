number = int(input('Number: '))

try:
    a = 10 / number
    print('Valid division!')
except ZeroDivisionError as zd:
    print(zd)

finally:
    print('Final result...')
