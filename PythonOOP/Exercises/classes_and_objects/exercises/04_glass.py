class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml):
        free_space = self.capacity - self.content
        if free_space >= ml:
            self.content += ml
            return f"Glass filled with {ml} ml"
        return f"Cannot add {ml} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        free_space = self.capacity - self.content
        return f"{free_space} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
