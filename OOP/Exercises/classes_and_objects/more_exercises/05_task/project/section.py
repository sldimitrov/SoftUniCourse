from typing import List
from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {Task.details(new_task)} is added to the section"

    def complete_task(self, task_name: Task) -> str:
        try:
            curr_task = next(filter(lambda t: t.name == task_name, self.tasks))
        except StopIteration:
            return f"Could not find task with the name {task_name}"

        task_name.completed = True

        return f"Completed task {task_name}"

    def clean_section(self):
        deleted_tasks_counter = 0
        for task in self.tasks:
            if task.completed:
                deleted_tasks_counter += 1
                self.tasks.remove(task)

        return f"Cleared {deleted_tasks_counter} tasks."

    def view_section(self):
        tasks_with_details = '\n'.join(t.details() for t in self.tasks)
        return f"Section {self.name}:\n" \
               f"{tasks_with_details}"
