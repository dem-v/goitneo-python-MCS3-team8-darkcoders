from .Command import Command


class SearchNotesCommand(Command):
    def prepare_parser(self, parser):
        super().prepare_parser(parser)
        parser.add_argument("-q", "--query", help="Search query for note content")
        parser.add_argument("-tg", "--tag", help="Search notes by a specific tag")

    def validate_args(self, args):
        if args.query is None:
            return "-q or --query parameter is required"

        return None

    def execute(self, address_book, note_book, args):
        if args.tag:
            matching_records = note_book.search_by_tag(args.tag)
            return "\n".join(
                [f"{index}. {record}" for index, record in matching_records.items()]
            )
        elif args.query:
            return "\n".join(
                [
                    f"{index}. {record}"
                    for index, record in note_book.search_records(args.query).items()
                ]
            )
        else:
            return "Please provide a search query or tag."
