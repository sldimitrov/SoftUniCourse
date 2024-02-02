import datetime

# Start a timer
start = datetime.datetime.now()

# Read User input
numbers = input().split()

# Print User output
print(*reversed(numbers))

# Countdown stops 
end = datetime.datetime.now()

# Taken time
print(end - start)  # - 0:00:01.678697
