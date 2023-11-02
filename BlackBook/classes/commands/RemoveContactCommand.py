from .Command import Command
from ..query.Query import Query
from ..query.QueryField import QueryField

class RemoveContactCommand(Command):

    def validate_args(self, args):
        if args.name == None:
            return '-n or --name parameter is required'

        return None

    def prepare_parser(self, parser):
        parser.add_argument("-n", "--name", help="")

    def execute(self, address_book, note_book, args):
        removed_count = address_book.remove_records(
            Query(
                name=QueryField(args.name),
            ),
        )
        if removed_count == 0:
            return "No records were removed."

        return F'Successfully removed {removed_count} records'
