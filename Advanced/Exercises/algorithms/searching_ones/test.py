my_dict = {'a': 1, 'b': 2, 'c': 3}
new_dict = {}
for key, value in my_dict.items():
    if value % 2 == 0:
        new_dict.setdefault('even', []).append(key)
    else:
        new_dict.setdefault('odd', []).append(key)

print(new_dict)

