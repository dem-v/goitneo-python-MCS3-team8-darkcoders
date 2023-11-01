from classes import KeyExistInContacts, KeyNotExistInContacts, input_error
from classes import DefaultExecutionDict
from classes import Record
from classes import AddressBook
from constants import MAX_DELTA_DAYS, WEEKDAYS_LIST


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    if cmd == "add-note":
        return cmd, " ".join(args)  # Об'єднайте всі аргументи у текст нотатки
    return cmd, *args


@input_error
def write_contact(contacts, args, is_change=False, *_):
    if len(args) != 2:
        raise IndexError()
    name, phone = args

    rec = contacts.find(name)
    if rec is not None and not is_change:
        raise KeyExistInContacts(name)
    elif rec is None and is_change:
        raise KeyNotExistInContacts(name)

    if not is_change:
        rec = Record(name)
        a = rec.add_phone(phone)
        if a is not None:
            return a
        contacts.add_record(rec)
    else:
        if len(rec.phones) == 0:
            return f"Contact {name} doesn't have phone numbers."
        a = rec.edit_phone(str(rec.phones[0]), phone)
        if a is not None:
            return a

    return f"Contact {name} {'changed' if is_change else 'added'}."


@input_error
def write_contact_add(contacts, args, *_):
    if len(args) != 2:
        raise IndexError()
    name, phone = args

    rec = contacts.find(name)
    if rec is not None:
        raise KeyExistInContacts(name)

    rec = Record(name)
    a = rec.add_phone(phone)
    if a is not None:
        return a
    contacts.add_record(rec)

    return f"Contact {name} added."


@input_error
def write_contact_change(contacts, args, *_):
    if len(args) != 3:
        raise IndexError()
    name, phone_old, phone_new = args

    rec = contacts.find(name)
    if rec is None:
        raise KeyNotExistInContacts(name)

    if len(rec.phones) == 0:
        return f"Contact {name} doesn't have phone numbers."
    p = rec.find_phone(phone_old)
    if p is None:
        return f"Contact {name} doesn't have phone number {phone_old}."
    a = rec.edit_phone(str(p), phone_new)
    if a is not None:
        return a

    return f"Contact {name} updated."


@input_error
def get_phone(contacts, args, *_):
    name = args[0]
    if name not in contacts.keys():
        raise KeyNotExistInContacts(name)
    return f"{contacts[name]}"


@input_error
def add_birthday(contacts: AddressBook, args, *_):
    if len(args) != 2:
        raise IndexError()
    name, birthday = args

    rec = contacts.find(name)
    if rec is None:
        raise KeyNotExistInContacts(name)

    a = rec.add_birthday(birthday)
    if a is not None:
        return a
    return f"Set birthday for contact {name} at {birthday}."


@input_error
def get_birthday(contacts, args, *_):
    name = args[0]
    rec = contacts.find(name)
    if rec is None:
        raise KeyNotExistInContacts(name)
    return f"Birthday of {name} is at {rec.show_birthday()}"


@input_error
def add_note(contacts, args, *_):
    if len(args) < 1:
        return "Please provide an argument for 'add-note'."

    arg = args[0]
    if " " not in arg:
        return "Invalid argument format. Please provide an argument in the format 'name note_text'."

    name, note = arg.split(" ", 1)
    rec = contacts.find(name)
    if rec is None:
        raise KeyNotExistInContacts(name)

    rec.add_note(note)
    return f"Note added for contact {name}."


@input_error
def edit_note(contacts, args):
    if len(args) < 3:
        raise ValueError("Usage: edit-note <contact_name> <note_index> <new_note_text>")

    name = args[0]
    note_index = int(args[1]) - 1  # Відніміть 1, щоб перевести в 0-індекс
    new_note_text = " ".join(args[2:])
    rec = contacts.find(name)

    if rec is None:
        raise ValueError(f"Contact {name} not found.")

    if 0 <= note_index < len(rec.notes):
        rec.notes[note_index].text = new_note_text
        return f"Note edited for contact {name}."
    else:
        raise ValueError("Note index out of range.")


@input_error
def remove_note(contacts, args, *_):
    if len(args) < 1:
        return "Please provide an argument for 'remove-note'."

    name = args[0]
    if len(args) > 1:
        note = args[1]
    else:
        note = None

    rec = contacts.find(name)
    if rec is None:
        raise KeyNotExistInContacts(name)

    if note is not None:
        rec.remove_note(note)
        return f"Note removed for contact {name}."
    else:
        return f"Please provide a note to remove for contact {name}."


@input_error
def get_notes(contacts, args, *_):
    name = args[0]
    rec = contacts.find(name)
    if rec is None:
        raise KeyNotExistInContacts(name)

    notes = rec.get_notes()
    if not notes:
        return f"No notes found for contact {name}."
    return "\n".join(notes)


def show_all_birthdays_for_week(contacts: AddressBook, *_):
    return contacts.get_birthdays_per_week(MAX_DELTA_DAYS, WEEKDAYS_LIST)


def print_phonebook(contacts, *_):
    return "\n".join(["{}".format(v) for _, v in contacts.items()])


def print_goodbye(*_):
    return "Good bye!"


def print_hello(*_):
    return "How can I help you?"


def print_bad(*_):
    return "Invalid command."


OPERATIONS = DefaultExecutionDict(
    {
        "close": print_goodbye,
        "exit": print_goodbye,
        "hello": print_hello,
        "add": write_contact_add,
        "change": write_contact_change,
        "phone": get_phone,
        "all": print_phonebook,
        "add-birthday": add_birthday,
        "show-birthday": get_birthday,
        "birthdays": show_all_birthdays_for_week,
        "add-note": add_note,
        "edit-note": edit_note,
        "remove-note": remove_note,
        "get-notes": get_notes,
    }
)

DEFAULT_METHOD = print_bad
