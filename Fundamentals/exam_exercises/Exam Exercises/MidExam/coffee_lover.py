# Define a function
def include_func(coffee_type, coffee_list: list):
    """
    Add the exact coffee at the end of your list.
    """
    coffee_list.append(coffee_type)
    return coffee_list


def remove_func(start_or_end: str, number_of_coffees: int, coffee_list: list):
    if 'first' in start_or_end:
        if len(coffee_list) > number_of_coffees:
            new_list = coffee_list.copy()
            counter = 0
            for drink in coffee_list:
                new_list.remove(drink)
                counter += 1
                if counter >= number_of_coffees:
                    break
            return new_list

    elif 'last' in start_or_end:
        if len(coffee_list) > number_of_coffees:
            counter = 0
            another_list = coffee_list.copy()
            coffee_list.reverse()

            for drink in coffee_list:
                another_list.remove(drink)
                counter += 1
                if counter >= number_of_coffees:
                    break
            return another_list
    return True


def prefer_func(index1: int, index2: int, coffee_list: list):
    """
    If both coffee indexes exist in your list, take the
    two coffees and change their places.
    otherwise - skip.
    """
    if 0 <= index1 < len(coffee_list):
        if 0 <= index2 < len(coffee_list):
            coffee_list[index1], coffee_list[index2] = coffee_list[index2], coffee_list[index1]
            return coffee_list
    return True


def reverse_func(coffee_list: list) -> list:
    """
    Reverse the order of the coffees.
    """
    coffee_list.reverse()
    return coffee_list


list_of_coffees = input().split()
number_of_operations = int(input())
for operation in range(number_of_operations):
    operator = input()
    if 'Include' in operator:
        coffee = (operator.split()[1])
        include_func(str(coffee), list_of_coffees)

    elif 'Remove' in operator:
        starting = (operator.split()[1])
        number = (operator.split()[2])
        list_of_coffees = remove_func(starting, int(number), list_of_coffees)

    elif 'Prefer' in operator:
        first_index = (operator.split()[1])
        second_index = (operator.split()[2])
        prefer_func(int(first_index), int(second_index), list_of_coffees)

    elif 'Reverse' in operator:
        reverse_func(list_of_coffees)

# Print the output
print("Coffees:")
print(' '.join(list_of_coffees))
