
people = {'Peter': 21, 'George': 18, 'John': 45}

# sort by age
print(sorted(people.items(), key=lambda kvp: kvp[1]))

# How to reverse ONLY INTEGERS
# print(sorted(people.items(), key=lambda kvp: -kvp[1]))

# How to reverse at all
# print(sorted(people.items(), key=lambda kvp: kvp[1], reverse=True))

# Sort the dict by names reversely
print(sorted(people.items(), key=lambda kvp: kvp[0], reverse=True))













