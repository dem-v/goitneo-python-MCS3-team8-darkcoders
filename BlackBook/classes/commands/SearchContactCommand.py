from .Command import Command
from ..query.Query import Query
from ..query.QueryField import QueryField


class SearchContactsCommand(Command):
    def prepare_parser(self, parser):
        parser.add_argument("-n", "--name", help="")
        parser.add_argument("-e", "--email", help="")
        parser.add_argument("-p", "--phone", help="")
        parser.add_argument("-b", "--birthday", help="")
        parser.add_argument("-a", "--address", help="")

    def execute(self, address_book, note_book, args):
        query = Query(
            name=QueryField(args.name, full_match=False, case_sensitive=False)
            if args.name is not None
            else None,
            email=QueryField(args.email, full_match=False, case_sensitive=False)
            if args.email is not None
            else None,
            phone=QueryField(args.phone, full_match=False, case_sensitive=False)
            if args.phone is not None
            else None,
            birthday=QueryField(args.birthday, full_match=False, case_sensitive=False)
            if args.birthday is not None
            else None,
            address=QueryField(args.address, full_match=False, case_sensitive=False)
            if args.address is not None
            else None,
        )

        records = address_book.search_records(query)
        return "\n".join([str(record) for record in records])
