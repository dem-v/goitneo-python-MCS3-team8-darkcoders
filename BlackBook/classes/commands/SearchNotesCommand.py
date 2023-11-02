from .Command import Command


class SearchContactsCommand(Command):
    def prepare_parser(self, parser):
        parser.add_argument("-q", "--query", help="")

    def validate_args(self, args):
        if args.query is None:
            return "-t or --text parameter is required"

        return None

    def execute(self, address_book, note_book, args):
        records = note_book.search_records(args.query)
        return "\n".join(
            [f"{index}. {record}" for index, record in records.items()]
        )
