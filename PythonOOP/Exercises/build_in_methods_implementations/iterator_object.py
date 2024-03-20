class custom_range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        temp = self.current
        if self.current <= self.end:
            self.current += 1
            return temp
        raise StopIteration

