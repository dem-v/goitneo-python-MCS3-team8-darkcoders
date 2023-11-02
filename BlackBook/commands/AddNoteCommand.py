from classes import NoteField
from .Command import Command


class AddNoteCommand(Command):
    def prepare_parser(self, parser):
        parser.add_argument("-t", "--text", help="Note text", required=True)
        parser.add_argument(
            "-g", "--tags", help="Comma-separated tags for the note")

    def validate_args(self, args):
        if args.name is None:
            return "-t or --text parameter is required"

        return None

    def execute(self, address_book, note_book, args):
        tags = args.tags.split(',') if args.tags else []
        note_text = NoteField(args.text, tags)
        note_book.add_record(note_text)

        return "Note successfully added with tags" if tags else "Note successfully added"
