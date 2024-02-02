numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

# numbers --> keys
# letters --> values
zipped = zip(numbers, letters)

print(dict(zipped))   # returns a dict

type(zipped)   # <class 'zip'>
