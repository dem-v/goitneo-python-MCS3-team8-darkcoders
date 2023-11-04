from .Command import Command
from classes import NoteField, split_tags


class EditNoteCommand(Command):
    def prepare_parser(self, parser):
        parser.add_argument("-i", "--id", help="Note ID to replace")
        parser.add_argument("-t", "--text", help="Note text")
        parser.add_argument("-tg", "--tags", nargs="*", help="Tags to add")

    def validate_args(self, args):
        if args.id is None:
            return "-i or --id parameter is required"

        return None

    def execute(self, address_book, note_book, args):
        note_id = int(args.id)
        note = note_book.data[note_id]

        if args.text:
            note.text = args.text

        if args.tags:
            note.tags = split_tags(args.tags)

        note_book.edit_record(note_id, note)

        return f"Note id {note_id} updated."
