#add squares less than 100
square = (i*i for i in count())
bounded_squares = takewhile(lambda x : x< 100, square)
total = 0
for i in bounded_squares:
        total += i