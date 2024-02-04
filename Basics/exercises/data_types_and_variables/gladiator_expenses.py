# Read User input
lost_fights_counts = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
# Logic
helmet_repairs = lost_fights_counts // 2
sword_repairs = lost_fights_counts // 3
shield_repairs = lost_fights_counts // (2 * 3)
armor_repairs = shield_repairs // 2
# Total
attributes = helmet_repairs * helmet_price\
             + sword_repairs * sword_price\
             + shield_repairs * shield_price\
             + armor_repairs * armor_price
print(f'Gladiator expenses: {attributes:.2f} aureus')
# Print User output