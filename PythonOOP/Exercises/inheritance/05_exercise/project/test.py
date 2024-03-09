import unittest

from project.drink import Drink
from project.food import Food
from project.product import Product
from project.product_repository import ProductRepository


class Tests(unittest.TestCase):
    def test_shop(self):
        food = Food('apple')
        drink = Drink('water')   
        repo = ProductRepository()
        repo.add(food)
        repo.add(drink)
        self.assertEqual(repo.products, [food, drink])
        repo.find("apple").decrease(5)
        self.assertEqual(str(repo), 'apple: 10\nwater: 10')


if __name__ == "__main__":
   unittest.main()