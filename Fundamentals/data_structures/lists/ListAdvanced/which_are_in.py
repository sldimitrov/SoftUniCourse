first_sequence = input().split(", ")
second_sequence = input().split(", ")

substring_list = []

for each in first_sequence:
    for word in second_sequence:
        if each in word:
            substring_list.append(each)
            break
print(substring_list)