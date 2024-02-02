import math
# Read User input
days = int(input())
food = float(input())

total_food_eaten = 0
cookies_eaten = 0;
d1 = 0
c1 = 0;
# Logic
for i in range (1, days + 1):
    food_eaten_dog = int(input())
    d1 += food_eaten_dog
    food_eaten_cat = int(input())
    c1 += food_eaten_cat
    food_eaten_per_day = food_eaten_cat + food_eaten_dog
    if i % 3 == 0:
        cookie = food_eaten_per_day / 10
        cookies_eaten += cookie
    total_food_eaten += food_eaten_per_day

percent_of_all_food_eaten = total_food_eaten / food * 100
percent_for_dog = d1 / total_food_eaten * 100
percent_for_cat = c1 / total_food_eaten * 100

print("Total eaten biscuits:", "%2.fgr." % math.ceil(cookies_eaten))
print("%.2f" % percent_of_all_food_eaten + "% of the food has been eaten.")
print("%.2f" % percent_for_dog + "% eaten from the dog.")
print("%.2f" % percent_for_cat + "% eaten from the cat.")
# Print User output