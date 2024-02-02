nums = input().split()
my_list = []
for num in nums:
    my_list.append(int(num))
n = int(input())
for _ in range(n):
    my_list.remove(min(my_list))
print(*my_list, sep=', ')
