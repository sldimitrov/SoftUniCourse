# Read User input
divisor = int(input())   # find N that is divisible by <---
boundary = int(input())  # less than or equal to <---
# Logic                  # greater than 0
biggest_divisor = 0;
for i in range(divisor, boundary + 1):
    if i % divisor == 0:
        biggest_divisor = i

print(biggest_divisor)
# Print User output