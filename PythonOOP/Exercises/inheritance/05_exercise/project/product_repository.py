from project.product import Product
from project.drink import Drink
from project.food import Food


class ProductRepository:

    def __init__(self):
        self.products: list[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            product_as_str = product.__str__()
            if product_as_str == product_name:
                return product

    def remove(self, product_name: str):
        for product in self.products:
            product_as_str = product.__str__()
            if product_as_str == product_name:
                self.products.remove(product)

    def __repr__(self):
        result = []

        for product in self.products:
            result.append(f"{product.name}: {product.quantity}")

        return '\n'.join(result)
