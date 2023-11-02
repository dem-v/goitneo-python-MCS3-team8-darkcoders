from .Command import Command
from classes import Query, QueryField, split_phones


class EditContactCommand(Command):
    def prepare_parser(self, parser):
        parser.add_argument("-q", "--query", help="Full contact name")
        parser.add_argument("-n", "--name", help="")
        parser.add_argument("-e", "--email", help="")
        parser.add_argument("-p", "--phones", help="")
        parser.add_argument("-rp", "--replace_phone", help="")
        parser.add_argument("-b", "--birthday", help="")
        parser.add_argument("-a", "--address", help="")

    def execute(self, address_book, note_book, args):
        updated_count = address_book.edit_records(
            Query(
                name=QueryField(args.query, full_match=True, case_sensitive=True),
            ),
            name=args.name,
            phones=split_phones(args.phones) if args.phones is not None else [],
            email=args.email,
            address=args.address,
            birthday=args.birthday,
            replace_phone=split_phones(args.replace_phone)
            if args.replace_phone is not None
            else None,
        )
        if updated_count == 0:
            return f'Couldn\'t find any records with the name "{args.query}".'

        return f"Successfully updated {updated_count} records"
