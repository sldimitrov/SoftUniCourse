import re


regex = r'((w{3})\.([A-Za-z0-9\-]+)(\.[a-z][\-\.a-z]*))'
text = input()
while text:
    if text:
        valid_emails = re.search(regex, text)
        if valid_emails:
            print(valid_emails.group(0))

    text = input()