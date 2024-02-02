


# Check for key existence by using the keys() method
my_dict = {'name': 'Peter', 'age': 22}
if 'name' in my_dict.keys(): # You can skip keys()
    print(my_dict['name'])


# Check for value existence by using the values() method
my_dict = {'name': 'Peter', 'age': 22}
if 22 in my_dict.values():
    print('22 is a value in the dictionary')