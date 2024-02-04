# Read User input
number_of_loaves = 0
colored_eggs = 0
money_spent = 0
budget = float(input())
price_for_1kg_flour = float(input())
# Logic
price_for_1pack_eggs = price_for_1kg_flour * 0.75
price_for_1l_milk = price_for_1pack_eggs * 1.25
loaves = budget / (price_for_1l_milk + price_for_1pack_eggs + price_for_1l_milk / 4)
print(loaves)

# Print User output