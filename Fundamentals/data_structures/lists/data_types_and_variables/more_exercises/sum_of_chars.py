# Read User input
n_lines = int(input())
total_sum = 0
# Logic
for char in range(n_lines):
    chr = input()
    total_sum += ord(chr)

print(f"The sum equals: {total_sum}")
# Print User output