
# Define class
class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.start = 0 - step
        self.curr = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.curr += 1
        self.start += self.step
        while self.curr < self.count:
            return self.start
        raise StopIteration


numbers = take_skip(10, 5)
for number in numbers:
    print(number)

