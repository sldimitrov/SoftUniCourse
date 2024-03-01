class Hero:
    # Initialisator
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    # Method
    def defend(self, damage: int):
        # Defend the hero
        self.health -= damage  # decrease his health

        if self.health <= 0:  # check if he is dead
            self.health = 0
            return f"{self.name} was defeated"

    # Method
    def heal(self, amount: int):
        # Heal our hero
        self.health += amount  # increase his health


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))
