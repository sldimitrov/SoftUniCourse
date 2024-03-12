from project.room import Room


class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms: list[Room] = []
        self.guests: int = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        instance_name = f"{stars_count} stars Hotel"
        return cls(instance_name)

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))
        except StopIteration:
            return

        result = room.take_room(people)

        if not result:
            self.guests += people

    def free_room(self, room_number):
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))
        except StopIteration:
            return

        people = room.guests
        result = room.free_room()

        if not result:
            self.guests -= people

    def status(self):
        information = f"Hotel {self.name} has {self.guests} total guests\n"

        free_rooms_numbers = [r.number for r in self.rooms if not r.is_taken]
        information += f"Free rooms: {', '.join([str(n) for n in free_rooms_numbers])}\n"

        taken_rooms_numbers = [r.number for r in self.rooms if r.is_taken]
        information += f"Taken rooms: {', '.join([str(n) for n in taken_rooms_numbers])}\n"

        return information
