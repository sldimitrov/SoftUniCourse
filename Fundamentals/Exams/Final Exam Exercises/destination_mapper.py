import re


text = input()

regex = r"([=|\/])([A-Z][A-Za-z]{3,})\1"
destinations = re.finditer(regex, text)

places = []
valid_destinations_sum = 0
for destination in destinations:
    places.append(destination[2])
    valid_destinations_sum += len(destination[2])

# Print the output
print(f"Destinations: {', '.join(places)}")
print(f'Travel Points: {valid_destinations_sum}')