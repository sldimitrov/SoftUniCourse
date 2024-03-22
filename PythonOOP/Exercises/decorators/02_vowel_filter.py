
def vowel_filter(function):
    vowels = ['a', 'e', 'y', 'i', 'o']

    def wrapper():
        letters = function()
        return [letter for letter in letters if letter in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())


