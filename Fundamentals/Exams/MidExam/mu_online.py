# Read User input
rooms = input().split("|")
health = 100
bitcoins = 0
have_been_killed = False
best_room = 0

for room in rooms:
    # the value is a string here
    command, value = room.split()
    best_room += 1

    if command == "potion":
        short_health = health
        health += int(value)
        if health > 100:
            health = 100
        difference = health - short_health
        print(f"You healed for {difference} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += int(value)
        print(f"You found {int(value)} bitcoins.")

    else:
        health -= int(value)
        if health > 0:
            print(f"You slayed {command}.")
        else:
            have_been_killed = True
            break

# Print User output
if not have_been_killed:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
else:
    print(f"You died! Killed by {command}.")
    print(f"Best room: {best_room}")




