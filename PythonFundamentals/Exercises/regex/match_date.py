import re


regex = r"\b(\d{2})(\/|\-|\.)([A-Z][a-z]{2})\2([\d]{4})\b"
text = input()
matches = re.findall(regex, text)

for match in matches:
    d = match[0]
    m = match[2]
    y = match[3]
    print(f"Day: {d}, Month: {m}, Year: {y}")