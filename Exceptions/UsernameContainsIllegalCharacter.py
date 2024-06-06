class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, arg, index):
        self.arg = arg
        self.index = index

    def __str__(self):
        return "The username contains an illegal character " + str(self.get_arg()) + " at index " + str(self.get_index())

    def get_arg(self):
        return self.arg

    def get_index(self):
        return self.index


class UsernameTooShort(Exception):
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return "The username %s is too short, it must be at least 3 characters long." % self.get_arg()

    def get_arg(self):
        return self.arg


class UsernameTooLong(Exception):
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return "The username %s is too long, it must be at most 16 characters long." % self.get_arg()

    def get_arg(self):
        return self.arg


class PasswordMissingCharacter(Exception):
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return "The password %s is missing a required character. " % self.get_arg()

    def get_arg(self):
        return self.arg


class PasswordTooShort(Exception):
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return "The password %s is too short, it must be at least 8 characters long. " % self.get_arg()

    def get_arg(self):
        return self.arg


class PasswordTooLong(Exception):
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return "The password %s is too long, it must be at most 40 characters long. " % self.get_arg()

    def get_arg(self):
        return self.arg


class UppercaseMissing(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)"


class LowercaseMissing(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Lowercase)"


class DigitMissing(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Digit)"


class SpecialMissing(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Special)"
