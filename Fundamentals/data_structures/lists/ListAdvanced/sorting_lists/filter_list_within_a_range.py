# Using lambda func withing a filter build-in function
# then using list to put the integers in a list
print(list(filter(lambda x: x % 2 == 0, range(23, 98))))

# However, a list comprehension would be a better choice:
print([x for x in range(23, 98) if x % 2 == 0])

