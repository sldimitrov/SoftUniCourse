# Define a function
def repeat_string(word: int, count: int):
    """
    :param word: Represents the string which we
    are going to repeat

    :param count: Represents the number of times
    we are going to write down the {word}

    :return: Word written down several(count) times
    """
    result = word * count
    return result


# Read User input
string = input()
counter = int(input())

# Call the function and print its result
print(repeat_string(string, counter))
