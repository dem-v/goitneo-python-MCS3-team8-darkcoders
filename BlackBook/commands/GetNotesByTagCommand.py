from .Command import Command


class GetNotesByTagCommand(Command):
    def prepare_parser(self, parser):
        parser.add_argument("-tg", "--tag", help="Tag to filter notes by")

    def validate_args(self, args):
        if not args.tag:
            raise ValueError("The --tag argument is required")

    def execute(self, address_book, note_book, args):
        notes_with_tag = note_book.search_by_tag(args.tag)
        return "\n".join(f"{index}. {note}" for index, note in notes_with_tag.items())
