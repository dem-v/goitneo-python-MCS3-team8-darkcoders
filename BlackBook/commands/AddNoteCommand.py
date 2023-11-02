from classes import NoteField
from .Command import Command


class AddNoteCommand(Command):
    def prepare_parser(self, parser):
        parser.add_argument("-t", "--text", help="Note text")

    def validate_args(self, args):
        if args.name is None:
            return "-t or --text parameter is required"

        return None

    def execute(self, address_book, note_book, args):
        note_text = NoteField(args.text)
        note_book.add_record(note_text)

        return "Note successfully added"
