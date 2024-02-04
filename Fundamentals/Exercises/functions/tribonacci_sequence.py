number_count = int(input())


# def tribonacci(count):
#     tribonacci_list = []
#     n = 0
#     while len(tribonacci_list) < number_count:
#         if n == 0:
#             tribonacci_list.append(1)
#         elif n == 1:
#             tribonacci_list.append(n)
#         elif n == 2:
#             tribonacci_list.append(n)
#         elif n > 2:
#             tribonacci_list.append(tribonacci_list[-1] + tribonacci_list[-2] + tribonacci_list[-3])
#         n += 1
#     return tribonacci_list
#
#
# print(*tribonacci(number_count), sep=" ")
# tribonacci_list = []
#
#
# def tribonacci(num):
#     if num == 1:
#         return 1
#     elif num == 2:
#         return 1
#     elif num == 3:
#         return 2
#     else:
#         return tribonacci(num - 1) + tribonacci(num - 2) + tribonacci(num - 3)
#
#
# for n in range(1, number_count + 1):
#     tribonacci_list.append(tribonacci(n))
#
# print(*tribonacci_list, sep=" ")

def tribonacci_recursive(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    elif n == 3:
        return [1, 1, 2]
    else:
        trib = tribonacci_recursive(n - 1)
        next_trib = trib[-3] + trib[-2] + trib[-1]
        trib.append(next_trib)
        return trib


n = int(input())

tribonacci_sequence = tribonacci_recursive(n)
print(" ".join(map(str, tribonacci_sequence)))