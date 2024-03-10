from project.animal import Animal


class Cheetah(Animal):
    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, 60)
