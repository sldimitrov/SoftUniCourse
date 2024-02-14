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
while True:
    if not textiles and not medicament:
        print("Textiles and medicaments are both empty.")
        break
    elif not textiles:
        print("Textiles are empty.")
        break
    elif not medicament:
        print("Medicaments are empty.")
        break
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
        combine -= 100
        medicament[-1] += combine
    else:
        med += 10
        medicament.append(med)


sorted_dict = sorted(healing_items.items(), key=lambda k: (-k[1], k[0]))
for item in sorted_dict:
    if int(item[1]) > 0:
        print(f"{item[0]} - {item[1]}")

if medicament:
    medicament.reverse()
    print(f"Medicaments left: {', '.join([str(x) for x in medicament])}")
if textiles:
    print(f"Textiles left: {', '.join([str(x) for x in sorted(textiles, reverse=True)])}")


