
class reverse_iter:
    def __init__(self, iterable: list):
        self.iterable = iterable
        self.length = len(iterable)
        self.end = self.length
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.end > self.start:
            self.end -= 1
            return self.iterable[self.end]
        raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
