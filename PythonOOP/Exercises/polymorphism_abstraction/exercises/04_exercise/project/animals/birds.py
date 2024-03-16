from project.animals.animal import Bird
from project.food import Food, Vegetable, Fruit, Meat, Seed


class Owl(Bird):

    def __init__(self, name: str, weight: float, wing_size, food_eaten: int = 0):
        super().__init__(name, weight, food_eaten)
        self.wing_size: float = wing_size

    @property
    def food_to_consume(self):
        return [Meat]

    @property
    def weight_increase(self):
        return 0.25

    def make_sound(self):
        return f"Hoot Hoot"


class Hen(Bird):

    def __init__(self, name: str, weight: float, wing_size, food_eaten: int = 0):
        super().__init__(name, weight, food_eaten)
        self.wing_size: float = wing_size

    @property
    def food_to_consume(self):
        return [Food, Vegetable, Fruit, Meat, Seed]

    @property
    def weight_increase(self):
        return 0.35

    def make_sound(self):
        return "Cluck"
