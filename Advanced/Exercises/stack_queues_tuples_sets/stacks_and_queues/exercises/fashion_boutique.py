# Read User input
clothes = [int(x) for x in input().split()]
rack_space = int(input())

racks_needed = 1
current_rack_space = rack_space

# Logic
while clothes:
    cloth = clothes.pop()

    if current_rack_space >= cloth:
        current_rack_space -= cloth
    else:
        racks_needed += 1
        current_rack_space = rack_space - cloth

# Print User output
print(racks_needed)



