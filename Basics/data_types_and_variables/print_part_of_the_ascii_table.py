# Read User input
start_index = int(input())
end_index = int(input())
# Logic
for i in range(start_index, end_index + 1):
    if i == end_index:
        print(chr(i))
    else:
        print(chr(i),end=' ')
# Print User output
