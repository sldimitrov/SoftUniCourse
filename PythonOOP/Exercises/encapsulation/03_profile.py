import re


class Profile:
    """
    Initialise a class - blueprint of User's profile
    """
    def __init__(self, username: str, password: str):
        """
        The constructor of the class - attach attributes to the instance
        """
        self.username = username
        self.password = password

    @property
    def username(self):
        """
        Initialise a getter method to return private attribute
        """
        return self.__username

    @username.setter
    def username(self, username):
        """
        Initialise a setter method to validate and create private attribute
        """
        if not 5 < len(username) < 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = username

    @property
    def password(self):
        """
        Initialise a getter method to return a private attribute
        """
        return self.__password

    @password.setter
    def password(self, password):
        """
        Initialise a setter method to validate and create private attribute
        """
        if len(password) < 8:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        regex_pattern = r"\d+"
        match = re.findall(regex_pattern, password)
        if not match:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        regex_patter = r"[A-Z]+"
        match = re.findall(regex_patter, password)
        if not match:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__password = password

    def __str__(self):
        """
        Override the string super method in order to return information when printing any attribute
        """
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
