class Cup:
    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

    def fill(self, value: int):
        space_left = self.size - self.quantity
        if space_left > value:
            self.quantity += value

    def status(self):
        space_left = self.size - self.quantity
        return space_left


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
