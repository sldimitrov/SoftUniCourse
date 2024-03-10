from project.food.food import Food


class Dessert(Food):
    def __init__(self, name: str, price: float, grams: float):
        super().__init__(name, price, grams)
        self.__calories: float = 0

    @property
    def calories(self):
        return self.__calories

