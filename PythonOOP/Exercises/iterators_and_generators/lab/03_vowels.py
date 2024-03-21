
class vowels:

    def __init__(self, text):
        self.text = text
        self.vowels: list = ['a', 'e', 'i', 'u', 'y', 'o']
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.vowels):
            return self.vowels[self.index]
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
