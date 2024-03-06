


class User:
    """
    Information for each of the library users will be stored
    """
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def info(self):
        return ', '.join(sorted(self.books))

    def __str__(self):
        if self.books:
            return f"{self.user_id}, {self.user_name}, {self.books}"
        else:
            return f"{self.user_id}, {self.user_name}, []"
