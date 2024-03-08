
class Hero:

    def __init__(self, username: str, level: int):
        self.username = username
        self.level = level

    def __str__(self):
        class_type = self.__class__
        return f"{self.username} of type {class_type.__name__} has level {self.level}"
