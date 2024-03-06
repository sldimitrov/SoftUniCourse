from collections import deque

# Read User input
materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())

# Initialise a dictionary for toys and their points
crafts = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

# Initialise a list for toys
toys = []

# Logic
while materials and magic_levels:
    material = materials.pop()
    magic = magic_levels.popleft()

    if material == 0 and magic == 0:  # if equal to 0
        continue                      # remove values

    # if one of the values is 0 continue
    if magic == 0:
        materials.append(material)
        continue
    if material == 0:
        magic_levels.appendleft(magic)
        continue

    # Find the multiplication
    production = material * magic
    if production < 0:  # if is lower than 0
        materials.append(material + magic)

    if production not in crafts.keys() and production > 0:
        materials.append(material + 15)  # if there is no match

    if production in crafts.keys():  # if we have match
        for k, v in crafts.items():
            if production == k:
                toys.append(v)  # append the toys into a list

# Print User output
if 'Bicycle' in toys and 'Teddy bear' in toys or 'Wooden train' in toys and 'Doll' in toys:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in sorted(materials, reverse= True)])}")
if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in sorted(magic_levels)])}")

for toy in sorted(set(toys)):
    print(f"{toy}: {toys.count(toy)}")