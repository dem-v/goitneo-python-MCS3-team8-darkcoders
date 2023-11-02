from .Command import Command
from ...classes import Record, split_phones, KeyExistInContacts


class AddContactCommand(Command):
    def prepare_parser(self, parser):
        parser.add_argument("-n", "--name", help="Contact name")
        parser.add_argument("-e", "--email", help="Contact email")
        parser.add_argument(
            "-p",
            "--phones",
            help="Contact phone: Must consist of 10 digits. Multiple phones are acceptable with space or comma separators.",
        )
        parser.add_argument(
            "-b", "--birthday", help="Contact birthday in format DD.MM.YYYY"
        )
        parser.add_argument("-a", "--address", help="Contact address")

    def validate_args(self, args):
        if args.name is None:
            return "-n or --name parameter is required"

        return None

    def execute(self, address_book, note_book, args):
        try:
            record = Record(
                name=args.name,
                phones=split_phones(args.phones),
                email=args.email,
                address=args.address,
                birthday=args.birthday,
            )
            address_book.add_record(record)

        except KeyExistInContacts:
            return f"AddressBook contains Record with name {args.name}"

        return "Contact successfully added"
