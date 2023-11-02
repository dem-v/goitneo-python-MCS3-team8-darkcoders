from .Command import Command


class RemoveNoteCommand(Command):
    def validate_args(self, args):
        if args.id is None:
            return "-i or --id parameter is required"

        return None

    def prepare_parser(self, parser):
        parser.add_argument("-i", "--id", help="Note ID to replace")

    def execute(self, address_book, note_book, args):
        note_book.remove_records(args.id)
        return f"Note {args.id} was removed."
