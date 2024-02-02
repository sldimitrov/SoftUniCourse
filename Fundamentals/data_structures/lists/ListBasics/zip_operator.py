numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)   # holds an iterator object

type(zipped)   # class 'zip'

# returns a list of tuples
print(dict(zipped))


