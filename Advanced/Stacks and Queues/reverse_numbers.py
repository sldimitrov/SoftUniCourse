import datetime

start = datetime.datetime.now()
# Read User input
numbers = input().split()

# Print User output
print(*reversed(numbers))

end = datetime.datetime.now()

print(end - start)
# Taken time - 0:00:01.678697