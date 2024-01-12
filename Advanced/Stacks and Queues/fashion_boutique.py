racks_needed = 1

# Read User input
box_of_clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

# Logic

# Free space
current_rack = rack_capacity
while box_of_clothes:
    # Space required
    current_cloth = box_of_clothes.pop()

    # If the required space is < or = than the free space:
    if current_cloth < current_rack:
        current_rack -= current_cloth  # decrease the free space
    else:
        # if the space required is more than the free one
        racks_needed += 1  # add a rack
        current_rack = rack_capacity

# Print User output
print(racks_needed)



