
def number_increment(numbers: list):

    def increase():
        return [el+1 for el in numbers]

    return increase()


print(number_increment([1, 2, 3]))