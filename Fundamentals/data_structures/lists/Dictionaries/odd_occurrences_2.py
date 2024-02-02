words = input().split()
words = [x.lower() for x in words]

clone_list = words.copy()

dictionary = {}
for word in words:
    counter = clone_list.count(word.lower())
    if counter % 2 != 0:
        dictionary[word] = counter
        clone_list.remove(word)

for key in dictionary.keys():
    print(key.lower(), end=' ')