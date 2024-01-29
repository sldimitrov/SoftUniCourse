numbers = input().split(', ')
n = int(input())

for _ in range(n):
    index = int(input())

    try:
        print(numbers[index])
        print(10/index)
    except IndexError:
        print('Index error')
    except ZeroDivisionError:
        print('Zero division error')