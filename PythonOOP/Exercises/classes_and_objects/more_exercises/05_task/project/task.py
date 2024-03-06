from typing import List


class Task:
    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments: List[str] = []
        self.completed = False

    def change_name(self, new_name: str):
        if self.name == new_name:
            return "Name cannot be the same."

        self.name = new_name
        return self.name

    def change_due_date(self, new_date: str):
        if self.due_date == new_date:
            return "Name cannot be the same."

        self.due_date = new_date
        return self.due_date

    def add_comment(self, new_comment):
        self.comments.append(new_comment)

    def edit_comment(self, comment_num: int, new_comment: str):
        try:
            self.comments[comment_num] = new_comment
        except IndexError:
            return "Cannot find comment."
        else:
            return ', '.join(self.comments)

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"

