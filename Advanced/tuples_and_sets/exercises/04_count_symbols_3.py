# Read User input
text = input()

# Logic
for symbol in sorted(set(text)):
    # Print User output
    print(f"{symbol}: {text.count(symbol)} time/s")

