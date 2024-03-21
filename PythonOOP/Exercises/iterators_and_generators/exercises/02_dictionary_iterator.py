
class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.pairs = dictionary.__iter__()
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        while self.idx <= len(self.dictionary):
            key = next(self.pairs)
            return key, self.dictionary[key]

        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)


