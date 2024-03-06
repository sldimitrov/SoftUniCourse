class Player:
    """
    Initialise Player class
    """
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: dict[str: int] = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int):
        """
        This method receives 3 arguments: self, skill_name and mana_cost.
        If the current player (self) doesn't have the current skill we add it
        to its skill set. Otherwise, we return an error message.
        """
        match = self.skills.get(skill_name)

        if match:
            return "Skill already added"
        self.skills[skill_name] = mana_cost  # add the ability
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        """
        This method receives self argument and returns info for the player
        """
        skill_set = [f"==={x} - {y}\n"for x, y in self.skills.items()]

        result = f"Name: {self.name}\n" \
                 f"Guild: {self.guild}\n" \
                 f"HP: {self.hp}\n" \
                 f"MP: {self.mp}\n" \
                 f"{''.join(skill_set)}"

        return result
