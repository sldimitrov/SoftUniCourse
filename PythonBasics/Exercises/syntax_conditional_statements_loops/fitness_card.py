# Read User input
money = float(input())
gender = input()
age = int(input())
sport = input()
# Logic
if gender == "m":
    if sport == "Gym":
        price = 42
    elif sport == "Boxing":
        price = 41
    elif sport == "Yoga":
        price = 45
    elif sport == "Yoga":
        price = 34
    elif sport == "Dances":
        price = 51
    elif sport == "Pilates":
        price = 39
elif gender == "f":
    if sport == "Gym":
        price = 35
    elif sport == "Boxing":
        price = 37
    elif sport == "Yoga":
        price = 42
    elif sport == "Yoga":
        price = 31
    elif sport == "Dances":
        price = 53
    elif sport == "Pilates":
        price = 37

if age < 19:
    price = price * 0.8
#Discount for 19y -
if money >= price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    difference = abs(price - money)
    print("You don't have enough money! You need $%.2f more." %difference)
# Print User output