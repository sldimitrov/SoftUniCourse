def sum_nums(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


sum_nums(**{'b': 1, 'c': 1, 'd': 1})