my_list = [1, 2, 3, 4, 5, 6, 'gosho']

# We print certain element's index by:
print(my_list.index(2))
print(my_list.index('gosho'))

# If we don't want to BOOM by index error
# we should use this variation
# better than try/except one
if 2 in my_list:
    print(my_list.index(2))
# In case we are not sure if the value
# really in the list or not
