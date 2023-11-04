from classes import NoteField, split_tags
from .Command import Command


class AddNoteCommand(Command):
    def prepare_parser(self, parser):
        super().prepare_parser(parser)
        parser.add_argument("-t", "--text", help="Note text")
        parser.add_argument("--tags", nargs="*", help="List of tags for the note")

    def validate_args(self, args):
        if args.text is None:
            return "-t or --text parameter is required"

        return None

    def execute(self, address_book, note_book, args):
        note_text = NoteField(args.text, split_tags(args.tags))
        note_book.add_record(note_text)

        if args.tags:
            return "Note successfully added with tags."
        else:
            return "Note successfully added."
