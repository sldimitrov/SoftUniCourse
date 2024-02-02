# Initialise a dictionary to store user data
phonebook = {}


# Define a function to search for contacts
# in the phonebook
def search_for_contact(number_of_searches):
    for search in range(number_of_searches):
        name = input('Enter the name you\'re searching for: ')
        # if name occurs in dictionary
        if name in phonebook.keys():
            # print info about him, the(value)
            print(f'{name} -> {phonebook[name]}')
        else:
            print(f'Contact {name} does not exist.')


# Define the main function
def main():
    user_input = input('\nTo add contact write - /name-number/ -\n'
                       'And to search for one enter the num of\n'
                       'searches, that you would like to execute: ')
    print()
    # While the user is adding a contact
    while not user_input.isnumeric():
        name, number = user_input.split('-')
        phonebook[name] = number
        user_input = input('To add contact write - /name-number/\n'
                           'And to search for one enter the num of\n'
                           'searches, that you would like to execute: ')
    search_for_contact(int(user_input))


if __name__ == '__main__':
    main()

print('\nThank you for using our Phonebook 1.2')
print(f"{'*' * 5}Stay tuned for new updates{'*' * 6}")
