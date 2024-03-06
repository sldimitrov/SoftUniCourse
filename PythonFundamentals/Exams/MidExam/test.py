number_of_coffees = 1

# List initializing
coffee_list = [1, 2, 3, 4, 5]
another_list = coffee_list.copy()
coffee_list.reverse()

counter = 0
for drink in coffee_list:
    another_list.remove(drink)
    counter += 1
    if counter == number_of_coffees:
        break
another_list.reverse()
print(another_list)
# print the output
