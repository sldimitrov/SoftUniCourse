

# Removes an item with a specified key name
students = {'name': 'George', 'course': 'Fundamentals'}
del students['course']
print(students)


# keyword can also delete the dictionary completely
students = {
    'first': 'Petkan',
    'second': 'Dragan',
    'third': 'Gosho'
}
del students
# print(students) --> NameError