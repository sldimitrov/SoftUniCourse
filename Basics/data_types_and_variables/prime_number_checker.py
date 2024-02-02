# Read User input
n = int(input())
is_prime = True
# Logic
for number in range(2, n):
    if n % number == 0:
        is_prime = False

print(is_prime)
# Print User output