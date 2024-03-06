def forecast(*weather_info):

    weather_table = {"Sunny": [], "Cloudy": [], "Rainy": []}

    for city, weather in weather_info:
        weather_table[weather].append(city)

    result = []

    for weather_type, towns in weather_table.items():
        for town in sorted(towns):
            result.append(f"{town} - {weather_type}")

    return '\n'.join(result)

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
