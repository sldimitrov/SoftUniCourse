key = int(input())
following_lines = int(input())
message = ""

for i in range(following_lines):
    lower_letter = input()
    decrypted_lower = chr(ord(lower_letter) + key)
    message += decrypted_lower

print(message)