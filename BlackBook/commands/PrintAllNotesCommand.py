from .Command import Command


class PrintAllNotesCommand(Command):
    def execute(self, address_book, note_book, args):
        return note_book.print_all_notes()
