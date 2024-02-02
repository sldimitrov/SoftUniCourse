# Read User input
numbers = [int(number) for number in input().split(", ")]
current_group = 10
while numbers:
    current_numbers = [number for number in numbers if number <= current_group]
    print(f"Group of {current_group}'s: {current_numbers}")
    current_group += 10
    numbers = [number for number in numbers if number not in current_numbers]
