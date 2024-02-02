my_dict = {'name': 'Jack', 'age': 26}

# Key can be used either inside square brackets or
# with the get() method
print(my_dict['name'])
my_dict.get('age')

# The return is NONE because
# the key does not exists
print(my_dict.get('address'))