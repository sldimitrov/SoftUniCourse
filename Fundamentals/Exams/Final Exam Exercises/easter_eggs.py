import re


dictionary = {}
regex = r"([@|#]{1,})([a-z]{3,})([#|@]{1,})([[\W]+]?[\/]{1,})([\d]+)([\/]{1,})"
text = input()
matches = re.findall(regex, text)
for match in matches:
    print(f'You found {match[4]} {match[1]} eggs!')