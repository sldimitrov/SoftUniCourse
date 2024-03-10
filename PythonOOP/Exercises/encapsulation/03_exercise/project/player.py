
class Player:
    """
    Initialise a class - blueprint of every player with his skills values
    """
    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
        # Attach private attributes to the object
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        """
        In order to access the private attribute - __name
        """
        return self.__name

    def __str__(self):
        """
        Override the build-in super method __str__ in order to represent players (object) skills (attributes) with print
        """
        player_info = f'Player: {self.__name}\n'
        player_info += f'Sprint: {self.__sprint}\n'
        player_info += f'Dribble: {self.__dribble}\n'
        player_info += f'Passing: {self.__passing}\n'
        player_info += f'Shooting: {self.__shooting}'

        return player_info


