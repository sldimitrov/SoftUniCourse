from project.animals.animal import Bird
from project.food import Food, Meat, Vegetable, Fruit, Seed


class Owl(Bird):

    @property
    def food_to_consume(self):
        return [Meat]

    @property
    def weight_increase(self) -> float:
        return 0.25

    @staticmethod
    def make_sound() -> str:
        return f"Hoot Hoot"


class Hen(Bird):

    @property
    def food_to_consume(self):
        return [Food, Vegetable, Fruit, Meat, Seed]

    @property
    def weight_increase(self) -> float:
        return 0.35

    @staticmethod
    def make_sound() -> str:
        return "Cluck"
