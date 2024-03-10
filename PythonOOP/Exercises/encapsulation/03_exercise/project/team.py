from project.player import Player


class Team:
    """
    Initialise a class - blueprint for Teams
    """
    def __init__(self, name: str, rating: int):
        # Initialise private attributes
        self.__name: str = name
        self.__rating: int = rating
        self.__players: list[Player] = []

    def add_player(self, player: Player):
        """
        Initialise a method to add players objects into the Team
        """
        player_match = [p for p in self.__players if p.name == player.name]
        if player_match:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        """
        Initialise a method to remove players objects from the Team
        """
        try:
            player = [p for p in self.__players if p.name == player_name][0]
            self.__players.remove(player)
            return player
        except IndexError:
            return f"Player {player_name} not found"

