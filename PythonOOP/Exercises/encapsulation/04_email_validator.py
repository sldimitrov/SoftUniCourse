
class EmailValidator:

    def __init__(self, min_length, mails, domains):
        self.min_length: int = min_length
        self.mails: list[str] = mails
        self.domains: list[str] = domains

    def __is_name_valid(self, name):
        return self.min_length <= len(name)

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        # Validate name
        name = email.split('@')[0]
        first_validation = self.__is_name_valid(name)

        # Validate mail
        mail = email.split('@')[1].split('.')[0]
        second_validation = self.__is_mail_valid(mail)

        # Validate domain
        domain = email.split('@')[1].split('.')[1]
        third_validation = self.__is_domain_valid(domain)

        return first_validation and second_validation and third_validation


# Test Code
mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
