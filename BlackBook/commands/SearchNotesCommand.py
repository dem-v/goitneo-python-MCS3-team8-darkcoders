from .Command import Command


class SearchNotesCommand(Command):
    def prepare_parser(self, parser):
        parser.add_argument(
            "-q", "--query", help="Query for searching notes by text")
        parser.add_argument("-t", "--tag", help="Search notes by tag")

    def validate_args(self, args):
        if args.query is None:
            return "-t or --text parameter is required"

        return None

    def execute(self, address_book, note_book, args):
        if args.tag:
            records = note_book.search_records(args.tag)
        elif args.query:
            records = note_book.search_records(args.query)
        else:
            return "Please provide a query or a tag for searching."

        return "\n".join([f"{index}. {record}" for index, record in records.items()])
