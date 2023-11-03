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


class NoteExists(Exception):
    pass


class NoteNotFound(Exception):
    pass


class NoteOperationError(Exception):
    pass


class ValidationException(Exception):
    def __init__(self, message):
        self.message = message


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
        except NoteExists as e:
            return f"Note already exists {e}."
        except NoteNotFound as e:
            return f"Note not found {e}."
        except NoteOperationError as e:
            return f"Note operation error {e}."

    return inner
