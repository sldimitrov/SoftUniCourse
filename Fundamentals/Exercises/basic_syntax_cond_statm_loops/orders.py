# Read User input
number_of_orders = int(input())
# Logic
total_price = 0
for i in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules_per_day <= 2000:
        order_price = price_per_capsule * capsules_per_day * days
        print(f"The price for the coffee is: $%.2f" % order_price)
        total_price += order_price
    else:
        continue
print(f'Total: $%.2f' % total_price)
# Print User output