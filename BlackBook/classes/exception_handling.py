class KeyExistInContacts(Exception):
    pass


class KeyNotExistInContacts(Exception):
    pass


class BadPhoneNumber(Exception):
    pass


class PhoneNumberIsMissing(Exception):
    pass


class BadBirthdayFormat(Exception):
    pass

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyExistInContacts as e:
            return f"This contact exists {e}."
        except KeyNotExistInContacts as e:
            return f"This contact does not exist {e}."
        except KeyError as e:
            return f"This contact does not exist {e}."
        except IndexError:
            return f"Bad arguments {args[1:]}."
        except BadPhoneNumber as e:
            return f"The phone number {e} does not match the requirements."
        except PhoneNumberIsMissing as e:
            return f"This number does not exist {e}."
        except BadBirthdayFormat as e:
            return f"Birthday format '{e}' is incorrect. It should be DD.MM.YYYY."

    return inner