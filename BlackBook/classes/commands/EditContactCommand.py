from .Command import Command
from ..query.Query import Query
from ..query.QueryField import QueryField

class EditContactCommand(Command):

    def prepare_parser(self, parser):
        parser.add_argument(
            "-q", "--query", help="Full contact name")
        parser.add_argument("-n", "--name", help="")
        parser.add_argument("-e", "--email", help="")
        parser.add_argument("-p", "--phones", help="")
        parser.add_argument("-rp", "--replace_phone", help="")
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
            phones=_split_phones(args.phones) if args.phones != None else [],
            email=args.email,
            address=args.address,
            birthday=args.birthday,
            replace_phone=_split_phones(
                args.replace_phone) if args.replace_phone != None else None
        )
        if updated_count == 0:
            return F"Couldn't find any records with the name \"{args.query}\"."

        return F'Successfully updated {updated_count} records'
