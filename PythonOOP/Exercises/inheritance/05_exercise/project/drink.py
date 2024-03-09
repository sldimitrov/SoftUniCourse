from project.product import Product


class Drink(Product):

    def __init__(self, name: str):
        super().__init__(name, quantity=10)

