import string
from UsernameContainsIllegalCharacter import *

def check_input(username, password):
    # Validate username
    try:
        valid_username(username)
    except Exception as e:
        print(e)
        return False

    # Validate password
    try:
        valid_password(password)
    except Exception as e:
        print(e)
        return False

    print("OK")
    return True


def valid_username(username):
    if len(username) < 3:
        raise UsernameTooShort(username)
    if len(username) > 16:
        raise UsernameTooLong(username)
    for index in range(len(username)):
        char = username[index]
        if not (char.isalnum() or char == '_'):
            raise UsernameContainsIllegalCharacter(char, index)
    return True


def valid_password(password):
    if len(password) < 8:
        raise PasswordTooShort(password)
    if len(password) > 40:
        raise PasswordTooLong(password)

    if not any(char.isupper() for char in password):
        raise UppercaseMissing(password)
    if not any(char.islower() for char in password):
        raise LowercaseMissing(password)
    if not any(char.isdigit() for char in password):
        raise DigitMissing(password)
    if not any(char in string.punctuation for char in password):
        raise SpecialMissing(password)

    return True


def main():
    result = False
    while not result:
        username = input("Enter your username")
        password = input("Enter your password")
        result = check_input(username, password)


if __name__ == "__main__":
    main()
