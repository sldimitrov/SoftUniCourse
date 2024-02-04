# Read User input
year = int(input())
year_is_special = False
# Logic
while not year_is_special:
    year += 1
    year_as_string = str(year)
    year_is_special = True
    for index in year_as_string:
        if year_as_string.count(index) != 1:
            year_is_special = False
            break

print(year)
# Print User output