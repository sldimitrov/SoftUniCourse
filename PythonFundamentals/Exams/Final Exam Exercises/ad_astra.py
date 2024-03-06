import re


def main_function():
    food_info = input()
    regex = r"(#|\|)([A-Za-z\s]+)\1([0-9]{2}\/[0-9]{2}\/[0-9]{2})\1([0-9]+)\1"
    valid_info = re.findall(regex, food_info)
    calculate_total_calories(valid_info)
    show_items_info(valid_info)


def calculate_total_calories(info):
    calories_for_a_day = 2000
    food_calories = 0
    # Calculate for how much days the calories are going to end
    for item in info:
        food_calories += int(item[3])
    survive_days = food_calories // calories_for_a_day
    print(f"You have food to last you for: {survive_days} days!")


def show_items_info(info):
    for item in info:
        print(f"Item: {item[1]}, Best before: {item[2]}, Nutrition: {item[3]}")


# Call the main function
main_function()


