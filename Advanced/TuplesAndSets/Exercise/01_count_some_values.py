numbers = [float(i) for i in input().split()]

for i in set(numbers):
    print(f"{i} - {numbers.count(i)}")
