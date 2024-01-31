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


def validate_email():
    pass


# def get_email():
command = input()
while command != "End":
    email = command

    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain = email.split('@')

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters!")
    if domain.split('.')[1] not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net!")
    if email.count('@') > 1:
        raise MoreThanOneAtSymbolError("Email should contain only one At symbol!")

    command = input()


def main():
    pass
    """
    (1) get email - get the password - validate each one.
    
    (2) add the User to the database (use one for real or something for improvised)
    
    (3) let the user to access something interesting for all that work he did
    passing all the exceptions
    
    (4) Show your self the fuck off boy
    """


