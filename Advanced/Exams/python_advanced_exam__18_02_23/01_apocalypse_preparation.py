from collections import deque

# Read the collections
textiles = deque([int(x) for x in input().split()])
medicament = [int(x) for x in input().split()]

# Healing items
healing_items = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0,
}

# Logic
while textiles and medicament:
    textile = textiles.popleft()
    med = medicament.pop()

    combine = textile + med

    if combine == 30:
        healing_items['Patch'] += 1
    elif combine == 40:
        healing_items['Bandage'] += 1
    elif combine == 100:
        healing_items['MedKit'] += 1
    elif combine > 100:
        healing_items['MedKit'] += 1
        left = combine - 100
        last_element = medicament.pop()
        last_element += left
        medicament.append(last_element)
    else:
        medicament.append(med + 10)

if not textiles and not medicament:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicament:
    print("Medicaments are empty.")

sorted_dict = sorted(healing_items.items(), key=lambda k: (-k[1], k[0]))

for k in sorted_dict:
    if k[1] != 0:
        print(f"{k[0]} - {k[1]}")

if medicament:
    print(f"Medicaments left: {', '.join([str(x) for x in sorted(medicament, reverse=True)])}")
if textiles:
    print(f"Textiles left: {', '.join([str(x) for x in sorted(textiles, reverse=True)])}")


