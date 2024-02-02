text = input().split()
new_list = []
for word in text:
    if len(word) % 2 == 0:
        new_list.append(word)

for element in new_list:
    print(element)