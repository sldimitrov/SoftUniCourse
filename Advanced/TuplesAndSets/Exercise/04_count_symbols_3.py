# Read User input
text = input()

# Logic
for symbol in sorted(set(text)):
    print(f"{symbol}: {text.count(symbol)} time/s")

