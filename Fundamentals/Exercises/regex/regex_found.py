import re


def regex_func(regex, string):
    match = re.search(regex, string)

    if match:
        print('match:', match.group())
    else:
        print('no match!')


regex_func('\d+', 'Slavcho123')  # numerical
regex_func('\D+', 'Slavcho123')   # non-numerical
regex_func('\\bworld\\b', 'hello world')  # end-boundary
