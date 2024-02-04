def weather_info(temp):
    c = convert_to_celsius(temp)
    if (c < 0):
        return f"{c} is freezing temperature"
    else:
        return f"{c} is above freezing temperature"


def convert_to_celsius(temperature):
    celsius = (temperature - 32) * (5 / 9)
    return celsius
