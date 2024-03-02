from project.player import Player


class Guild:

    def __init__(self, name: str,):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, name: str):
        try:
            self.players.remove(name)
        except KeyError:
            return f"Player {name} is not in the guild."
        else:
            return f"Player {name} has been removed from the guild."

    def guild_info(self):
        return f"Guild: {self.name}\n" \
               f"{''.join(f'{pl.player_info()}' for pl in self.players)}"


