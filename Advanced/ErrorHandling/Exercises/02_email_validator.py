class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass

# add extension for more
VALID_DOMAINS = ('com', 'bg', 'org', 'net')

command = input()
while command != "End":
    email = command

    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain = email.split('@')

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    if domain.split('.')[1] not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    command = input()



