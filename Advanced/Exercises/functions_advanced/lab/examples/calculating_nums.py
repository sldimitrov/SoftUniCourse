def addition(*args):
    total_sum = 0
    for n in args:
        total_sum += n
    return total_sum


# ARGS: takes 0, 1 or many arguments
# 0
print(addition())
# 1
print(addition(1))
# 10
print(addition(1, 2, 3, 4))


