from collections import deque

# Read collections
amount_of_money = [int(x) for x in input().split()]
food_prices = deque([int(x) for x in input().split()])

# Initialise a counter
food_eaten = 0

# Logic
while amount_of_money and food_prices:
    money = amount_of_money.pop()
    price = food_prices.popleft()

    if money == price:  # if they are equal
        food_eaten += 1

    elif money > price:  # if current money are more than the price
        food_eaten += 1
        # Calculate the change and add it to the last value within the collection
        change = money - price
        if amount_of_money:
            amount_of_money[-1] += change
        else: amount_of_money = change
    else:
        continue

# Print User output
if food_eaten >= 4:
    print(f"Gluttony of the day! Henry ate {food_eaten} foods.")
elif 1 < food_eaten < 4:
    print(f"Henry ate: {food_eaten} foods.")
elif food_eaten == 1:
    print(f"Henry ate: {food_eaten} food.")
elif not food_eaten:
    print("Henry remained hungry. He will try next weekend again.")