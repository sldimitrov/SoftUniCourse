
class Mammal:
    """
    Initialise a class that is a blueprint of animals that are Mammals
    """
    # Define a private class attribute
    __kingdom = 'animals'

    # Define a constructor
    def __init__(self, name: str, type: str, sound: str):
        # Attach attributes to the instance
        self.name = name
        self.type = type
        self.sound = sound

    def make_sound(self):
        """
        This method return the sound that the current animal makes
        """
        return f'{self.name} makes {self.sound}'

    def get_kingdom(self):
        """
        This method returns the name of the current animal kingdom
        """
        return self.__kingdom

    def info(self):
        """
        This method return the type of the current animal
        """
        return f'{self.name} is of type {self.type}'


# Test code

# Initialise an instance
mammal = Mammal("Dog", "Domestic", "Bark")

# Print the return of the methods below
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())

