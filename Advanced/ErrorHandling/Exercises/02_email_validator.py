import time


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class DomainMustContainsDot(Exception):
    pass


# add extension for more
VALID_DOMAINS = ('com', 'bg', 'org', 'net')


def greeting() -> bool:
    """
    This function is being called by the main, just after running the program.
    We use it to call the print message function and greet the User.
    """
    print_messages(greeting.__name__)

    # Ask the User if he is ready to start
    answer = input('Are you ready to start? (y/n): ')

    # continue the program if he agrees
    if answer.lower() == 'y' or answer.lower() == 'yes':
        return True

    # if the returns that he is not ready raise an exception
    elif answer.lower() == 'n' or answer.lower() == 'no':
        raise SystemExit

    else:  # in every other case the program continues
        print("Anyway, let's go")


def print_messages(func_name: str) -> None:
    """
    This function is being called from many others.
    Its purpose is to different print messages to the User,
    depending on the function which have called it.
    """
    message = ''
    # Print a message to greet the User
    if func_name == "greeting":
        message = (
            """
            Hello, Colleague!
            Welcome to my improvised User Authentication Project.
            Hope that you will like it. I will be very happy 
            to hear or read your recension about it.
            
            I know we live in world of imperfection and I am sure
            that we all have so much to improve, so please tell me:
            
            What do you think are my mistakes and how I should
            improve my ways of writing code or anything else.
            """
        )

    # Print a message about Valid Email Requirements
    if func_name == "get_email":
        message = (
            f"""
        {'<->-<->' * 6}
              !!!Valid Email Requirements!!!\n
            (1) It must consist only 1 At symbol '@'!
            (2) The length of its first part should
            be more than 4 characters!
            (3) Last but not least, the domain must
            be one of the following: {', '.join(VALID_DOMAINS)}!
                   !Warning! 
            If your email is invalid the program will
            throw you just like an exception!
                              !Warning!
            
        {'<->-<->' * 6}
            """
        )

    elif func_name == "get_password":
        message = (
            f"""
        {'<->-<->' * 6}
              !!!Rules about valid password!!!\n
            (1)
            
        {'<->-<->' * 6}
            """
        )

    print(message)


def get_email() -> str:
    """
    This function is being called by the main in order to get
    the email address of the user.

    It also calls the 1-(print_messages) and the 2-(is_email_valid) functions

    The first one prints out the email validation rules.

    If the second one returns true, the function returns the email to the main.
    """
    # Print info about the email validation
    print_messages(get_email.__name__)  # pass the current function name as an argument

    # Read User email
    user_email = input("Enter your email address, please: ")

    # Make validation of the email address
    if is_email_valid(user_email):
        # If the email is valid return it to main function
        return user_email


def is_email_valid(email: str) -> bool:
    """
    This function is being called by the (get_email) one.

    It checks if the email is invalid and if it is - the program stops.

    Otherwise, it returns True
    """

    # If there is not an At symbol - throw an exception
    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain at least one 'maimunsko' A!")

    # Split the email into 2 parts
    name, domain = email.split('@')

    if '.' not in domain:
        raise DomainMustContainsDot("Domain must contain a dot! '.com'")

    # Check if the length of the first part is shorter or equal to 4 and if it is - throw an exception
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters!")

    # Check if the last part of the domain is not in Valid Domains and if it is not - raise an exception
    elif domain.split('.')[1] not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net!")

    # Check if there is more than 1 At symbol - stop the program
    elif email.count('@') > 1:
        raise MoreThanOneAtSymbolError("Email must contain only one At symbol!")

    # The program was not stopped, so we have a valid email address:
    return True


def get_password():
    """
    This function is being called by the main in order to get
    the password of the user.

    If the password is valid, we ask the User to repeat
    his password in the console.

    If the User pass the authentication we return the password to the main
    """
    while True:
        # Read User password
        user_password = input("Create a password password: ")

        # Make validation of the password
        if is_password_valid(user_password):

            # Tell the User to repeat his password for security reasons
            repeat_valid_password = input("Repeat your password: ")

            # If password inputted matches return the password to the main
            if user_password == repeat_valid_password:
                return user_password
            else:
                print('Password does not match the previous one!\n'
                      'Please try again')


def is_password_valid(password) -> bool:
    """
    This function check if the password given by the User is valid or not.
    if valid: return: True,
    if not valid: return False,
    """
    # Initialise a boolean in order to know if the password is valid or not
    is_valid = True

    # Check the password length
    if not (4 < len(password) < 12):
        is_valid = False

    # Check the number of digits in it
    number_of_digits = [x for x in password if x.isdigit()]
    if len(number_of_digits) < 2:
        is_valid = False

    # Check if there is a capital letter in the password
    capital_letters = [x for x in password if x.capitalize()]
    if len(capital_letters) < 1:
        is_valid = False

    return is_valid  # boolean


def main():
    """
    (1) let the user access something interesting for all that work he did
    passing all the exceptions

    (2) add the User to the database (use one for real or something for improvised)

    (3) add encrypting of saved passwords

    (4) Add description of each function

    (4) Show your self the fuck off boy

    """
    # First greet the User
    greeting()

    # Read and Validate input
    email = get_email()
    password = get_password()

    # Store the Data



if __name__ == '__main__':
    main()
