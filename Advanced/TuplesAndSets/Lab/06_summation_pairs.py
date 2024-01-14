
# Time Complexity 0(n^2) WORST CASE

# Read User input
numbers = [int(x) for x in input().split()]
target_num = int(input())

unused_numbers = set(numbers)

# Logic
for a in numbers:
    for b in numbers:
        if a + b == target_num:
            if a and b in unused_numbers and a != b:

                # Print User output
                print(f"{a} + {b} = {target_num}")

                unused_numbers.remove(a)
                unused_numbers.remove(b)
