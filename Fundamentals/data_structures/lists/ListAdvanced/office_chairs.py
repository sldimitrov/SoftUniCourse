def office_chairs(room_number: int)-> str:
    chairs_left = 0
    for room in range(1, room_number + 1):
        chairs, num = input().split()
        difference = len(chairs) - int(num)
        if difference < 0:
            print(f'{abs(difference)} more chairs needed in room {room}')
        chairs_left += difference
    return chairs_left


# Read User input
number_of_rooms = int(input())
total_free_chairs = office_chairs(number_of_rooms)
if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")
