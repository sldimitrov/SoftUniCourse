
# Read User input
n = int(input())
guests = set()

# Logic
for _ in range(n):
    person = input()
    guests.add(person)

code = input()
while code != "END":
    if code in guests:
        guests.remove(code)
    code = input()

# Print User output
print(len(guests))
for guest in sorted(guests):
    print(guest)
