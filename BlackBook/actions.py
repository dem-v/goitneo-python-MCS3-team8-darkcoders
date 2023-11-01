from classes import *
from constants import MAX_DELTA_DAYS, WEEKDAYS_LIST
from abc import ABC, abstractmethod
import argparse


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
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
    }
)

DEFAULT_METHOD = print_bad


class Command:

    def validate_args(self, args):
        return None

    def executor(self, address_book, note_book, args):
        try:
            parser = argparse.ArgumentParser()
            self.prepare_parser(parser)
            parsed = parser.parse_args(args)
            error = self.validate_args(parsed)
            if error != None:
                return f'Error: {error}'

            return self.execute(address_book, note_book, parsed)

        except SystemExit:
            return None

    def prepare_parser(self, parser):
        pass

    @abstractmethod
    def execute(self, address_book, note_book, args):
        pass


class AddContactCommand(Command):

    def prepare_parser(self, parser):
        parser.add_argument("-n", "--name", help="", required=True)
        parser.add_argument("-e", "--email", help="")
        parser.add_argument("-p", "--phone", help="")
        parser.add_argument("-b", "--birthday", help="")
        parser.add_argument("-a", "--address", help="")

    def validate_args(self, args):
        if len(args.name) <= 2:
            return 'Name must have more than 2 symbols'

        return None

    def execute(self, address_book, note_book, args):
        address_book.add_record(
            Record(
                name=args.name,
                phone=args.phone,
                email=args.email,
                address=args.address,
                birthday=args.birthday,
            )
        )
        return 'Contact successfully added'


class EditContactCommand(Command):

    def prepare_parser(self, parser):
        parser.add_argument(
            "-q", "--query", help="Full contact name")
        parser.add_argument("-n", "--name", help="")
        parser.add_argument("-e", "--email", help="")
        parser.add_argument("-p", "--phone", help="")
        parser.add_argument("-b", "--birthday", help="")
        parser.add_argument("-a", "--address", help="")

    def execute(self, address_book, note_book, args):
        updated_count = address_book.edit_records(
            Query(
                name=QueryField(
                    args.query,
                    full_match=True,
                    case_sensitive=True
                ),
            ),
            name=args.name,
            phone=args.phone,
            email=args.email,
            address=args.address,
            birthday=args.birthday,
        )
        if updated_count == 0:
            return F"Couldn't find any records with the name \"{args.query}\"."

        return F'Successfully updated {updated_count} records'


class RemoveContactCommand(Command):

    def prepare_parser(self, parser):
        parser.add_argument("-n", "--name", help="")
        parser.add_argument("-e", "--email", help="")
        parser.add_argument("-p", "--phone", help="")
        parser.add_argument("-b", "--birthday", help="")
        parser.add_argument("-a", "--address", help="")

    def execute(self, address_book, note_book, args):
        removed_count = address_book.remove_records(
            Query(
                name=QueryField(args.name) if args.name != None else None,
                email=QueryField(args.email)if args.email != None else None,
                phone=QueryField(args.phone)if args.phone != None else None,
                birthday=QueryField(args.birthday)
                if args.birthday != None
                else None,
                address=QueryField(args.address)
                if args.address != None
                else None,
            ),
        )
        if removed_count == 0:
            return "No records were removed."

        return F'Successfully removed {removed_count} records'


class SearchContactsCommand(Command):

    def prepare_parser(self, parser):
        parser.add_argument("-n", "--name", help="")
        parser.add_argument("-e", "--email", help="")
        parser.add_argument("-p", "--phone", help="")
        parser.add_argument("-b", "--birthday", help="")
        parser.add_argument("-a", "--address", help="")

    def execute(self, address_book, note_book, args):
        query = Query(
            name=QueryField(
                args.name,
                full_match=False,
                case_sensitive=False
            ) if args.name != None else None,
            email=QueryField(
                args.email,
                full_match=False,
                case_sensitive=False
            )if args.email != None else None,
            phone=QueryField(
                args.phone,
                full_match=False,
                case_sensitive=False
            )if args.phone != None else None,
            birthday=QueryField(
                args.birthday,
                full_match=False,
                case_sensitive=False
            )
            if args.birthday != None
            else None,
            address=QueryField(
                args.address,
                full_match=False,
                case_sensitive=False
            )
            if args.address != None
            else None,
        )
        
        records = address_book.search_records(query)
        return f'Founded {len(records)}'
