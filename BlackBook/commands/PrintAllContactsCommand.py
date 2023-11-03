from .Command import Command


class PrintAllContactsCommand(Command):
    def execute(self, address_book, note_book, args):
        return address_book.print_all_contacts()
