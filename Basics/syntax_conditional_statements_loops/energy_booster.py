# Read User input
fruit = input()
size = input()
number = int(input())

# Logic
if size == "small":
  pieces = number * 2
  if fruit == "Watermelon":
    price = 56
  elif fruit == "Mango":
    price = 36.66
  elif fruit == "Pineapple":
    price = 42.10
  elif fruit == "Raspberry":
    price = 20
elif size == "big":
  pieces = number * 5
  if fruit == "Watermelon":
    price = 28.7
  elif fruit == "Mango":
    price = 19.6
  elif fruit == "Pineapple":
    price = 24.8
  elif fruit == "Raspberry":
    price = 15.2

total_price = price * pieces
if 400 <= total_price <= 1000:
    total_price = total_price * 0.85
elif total_price > 1000:
    total_price = total_price * 0.5
print("%.2f lv." % total_price)
# Print User output