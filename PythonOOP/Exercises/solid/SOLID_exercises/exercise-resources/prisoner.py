import copy


class Person:

    def __init__(self, position):
        self.position = position


class FreePerson(Person):

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist


class Prisoner(Person):
    PRISON_LOCATION = [3, 3]

    def __init__(self):
        super().__init__(copy.copy(self.PRISON_LOCATION))
        self.is_free = False

free_person = FreePerson([1, 3])

try:
    free_person.walk_east(5)
    print(f"Free person walks east")
except AttributeError:
    pass

prisoner = Prisoner()
print("The prisoner trying to walk to north by 10 and east by -3.")

try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
except AttributeError("Prisoner cannot exit the prison!"):
    pass

