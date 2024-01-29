number = int(input('Number: '))

try:
    a = 10 / number
    print('Valid division!')
except ZeroDivisionError:
    print('Zero division')

finally:
    print('Final result...')
