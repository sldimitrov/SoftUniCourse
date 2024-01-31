class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


# add extension for more
VALID_DOMAINS = ('com', 'bg', 'org', 'net')


def valid_email(email):
    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain = email.split('@')

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters!")
    elif domain.split('.')[1] not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net!")
    elif email.count('@') > 1:
        raise MoreThanOneAtSymbolError("Email should contain only one At symbol!")
    return True


def valid_password(password):
    pass


def get_email():
    # Read User email
    user_email = input("Enter your email address, please: ")

    # Make validation of the email address
    if valid_email(user_email):
        return user_email


def get_password():
    # Read User password

    while True:
        # Read User password
        user_password = input("Create a password password: ")

        # Make validation of the password
        if valid_password(user_password):
            # Tell the User to repeat his password for security reasons
            repeat_valid_password = input("Repeat your password: ")

            if user_password == repeat_valid_password:
                return user_password
            else:
                print('Password does not match the previous one!\n'
                      'Please try again')




def main():
    """
    (1) let the user access something interesting for all that work he did
    passing all the exceptions

    (2) add the User to the database (use one for real or something for improvised)

    (3) add encrypting of saved passwords

    (4) Show your self the fuck off boy

    """
    email = get_email()
    password = get_password()





