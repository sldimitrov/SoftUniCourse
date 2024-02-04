start_index = 97
end_index = 97 + int(input())

for i in range(start_index, end_index):
    for j in range(start_index, end_index):
        for k in range(start_index, end_index):
            print(chr(i) + chr(j) + chr(k))
