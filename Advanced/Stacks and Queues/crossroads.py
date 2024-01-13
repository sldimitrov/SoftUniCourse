from collections import deque

green_light = int(input())
free_window = int(input())

cars_passed = 0

cars = deque()
info = input()

while info != "END":
    if info != "green":
        cars.append(info)
    else:
        current_green_light = green_light

        while current_green_light > 0 and cars:
            car = cars.popleft()

            time = current_green_light + free_window
            if len(car) > time:
                print(f"A crash happened!\n{car} was hit at {car[time]}.")
                raise SystemExit

            current_green_light -= len(car)
            cars_passed += 1

    info = input()

print(f"Everyone is safe.\n{cars_passed} total cars passed the crossroads.")