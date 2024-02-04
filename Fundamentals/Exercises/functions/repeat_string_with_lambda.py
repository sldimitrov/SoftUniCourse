# Define lambda function
x = lambda word, count: word * number
"""
    This lambda function dublicates a string
    (count) times
    
    Parameters: word: string, count: int
    
    Returns a string which was being dublicates
    (count) number of times
"""
# Read User input
word = input()
number = int(input())

# Call the small anonymous function(lambda)
# And print its result
print(x(word, number))