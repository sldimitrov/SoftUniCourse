# Read User input
minutes_for_the_day_walk = int(input())
walks_per_day = int(input())
calories = int(input())
# Logic
total_minutes = walks_per_day * minutes_for_the_day_walk
total_calories_burned = total_minutes * 5
if calories * 0.5 <= total_calories_burned:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_calories_burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_calories_burned}.")
# Print User output