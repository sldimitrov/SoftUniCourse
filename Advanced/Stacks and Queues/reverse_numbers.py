from collections import deque

reversed_list = []

numbers = deque(input().split())

for n in numbers.copy():
    reversed_list.append(numbers.pop())

print(*reversed_list)