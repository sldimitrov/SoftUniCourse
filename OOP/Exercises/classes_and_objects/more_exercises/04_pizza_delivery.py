
class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def invalid_changes(self):
        return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def add_extra(self, ingredient: str, qnt: int, price_per_qnt: float):
        if self.ordered:
            return self.invalid_changes()

        if ingredient in self.ingredients:
            self.ingredients[ingredient] += qnt
            total_sum = qnt * price_per_qnt
            self.price += total_sum
        else:
            self.ingredients[ingredient] = qnt
            total_sum = qnt * price_per_qnt
            self.price += total_sum

    def remove_ingredient(self, ingredient: str, qnt: int, price_per_qnt: float):
        if self.ordered:
            return self.invalid_changes()

        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        elif qnt > self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"
        else:
            self.ingredients[ingredient] -= qnt
            price_diff = qnt * price_per_qnt
            self.price -= price_diff

    def make_order(self):
        if not self.ordered:
            self.ordered = True
            return f"You've ordered pizza {self.name} prepared with {', '.join([f'{k}: {v}' for k, v in self.ingredients.items()])} and the price will be {self.price}lv."
        else:
            self.invalid_changes()


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))
