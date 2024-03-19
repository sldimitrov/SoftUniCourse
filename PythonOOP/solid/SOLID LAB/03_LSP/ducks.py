from abc import abstractmethod, ABC


class DuckMixin:
    @staticmethod
    def shine():
        return (f"Every duck can shine."
                f"That's why we are creating a Mixin class"
                f"that every duck will be inherited from.")


class Duck(ABC, DuckMixin):

    @staticmethod
    @abstractmethod
    def quack():
        pass

    @staticmethod
    @abstractmethod
    def walk():
        pass

    @staticmethod
    @abstractmethod
    def fly():
        pass


class LakeDuck(Duck, DuckMixin):
    @staticmethod
    def quack():
        return "Quack quack"

    @staticmethod
    def walk():
        return "patiently walking"

    @staticmethod
    def fly():
        return "fly till I die"


class RubberDuck(DuckMixin):  # CANNOT INHERIT DUCK
    """ 3rd Principe
    Liskov substitution says that:
    ---Derived types must be completely substitutable for their base types.
    ---that is the reason that the rubber duck cannot inheritance from Duck (i.g. it cannot walk)
    """
    @staticmethod
    def quack():
        return "Squeak"


class RobotDuck(Duck, DuckMixin):  # INHERIT AND EXTEND THE LOGIC OF DUCK CLASS
    """
    Derived classes:
    ---only EXTEND functionalities of the base class.
    ---must NOT remove base class behaviour
    """
    HEIGHT = 50

    def __init__(self):
        self.height = 0

    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0


robot_duck = RobotDuck()

print(robot_duck.shine())
print(robot_duck.quack())


