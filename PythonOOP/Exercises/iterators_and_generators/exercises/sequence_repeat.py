
class sequence_repeat:
    def __init__(self, sequence, number: int):
        self.sequence = sequence
        self.number = number + 1
        self.counter = 0
        self.curr = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr < len(self.sequence) - 1:
            self.curr += 1
        else:
            self.curr = 0
        self.counter += 1
        while self.counter < self.number:
            return self.sequence[self.curr]
        raise StopIteration


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')

