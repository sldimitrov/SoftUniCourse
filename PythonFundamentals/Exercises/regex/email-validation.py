import re

email_date = ['valid123@email.bg', 'invalid*name@email.bg',
              'slavidimitrov06@abv.bg', 'nakoGeq#sixty.nine',
              'naskociganina@yahoo.email']

pattern = r'^^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$'

for email in email_date:
    if re.match(pattern, email):
        print(email)