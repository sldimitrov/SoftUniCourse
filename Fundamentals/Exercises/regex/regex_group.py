import re

text = 'The ball is red and big, end of text'
pattern = '(red|blue) and (big|small)'
result = re.findall(pattern, text)
print(result)