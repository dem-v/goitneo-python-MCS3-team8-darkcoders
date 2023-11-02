from .Command import Command
from classes import NoteField


class EditNoteCommand(Command):
    def prepare_parser(self, parser):
        parser.add_argument("-i", "--id", help="Note ID to replace")
        parser.add_argument("-t", "--text", help="Note text")

    def validate_args(self, args):
        if args.id is None:
            return "-i or --id parameter is required"
            
        if args.text is None:
            return "-t or --text parameter with the text to replace is required"

        return None

    def execute(self, address_book, note_book, args):
        note_book.edit_record(int(args.id), NoteField(args.text))

        return f"Note id {args.id} updated."
