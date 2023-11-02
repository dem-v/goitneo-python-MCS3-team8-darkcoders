from classes import (
    AddressBook,
    NoteBook,
    Storage,
)
from commands import (
    AddContactCommand,
    EditContactCommand,
    RemoveContactCommand,
    SearchContactsCommand,
    AddNoteCommand,
    EditNoteCommand,
    RemoveNoteCommand,
    SearchNotesCommand,
    HelloCommand,
    HelpCommand,
    PrintAllContactsCommand,
    PrintAllNotesCommand,
    PrintNotesWithTagsCommand,
    GetNotesByTagCommand,
)
from constants import BINARY_STORAGE_FILENAME, BINARY_NOTEBOOK_STORAGE_FILENAME
import re
import gnureadline


gnureadline.set_completer_delims(" \t\n;")

commands = {
    "add": AddContactCommand(),
    "delete": RemoveContactCommand(),
    "edit": EditContactCommand(),
    "search": SearchContactsCommand(),
    "addnote": AddNoteCommand(),
    "editnote": EditNoteCommand(),
    "removenote": RemoveNoteCommand(),
    "getnotes": SearchNotesCommand(),
    "hello": HelloCommand(),
    "help": HelpCommand(),
    "printcontacts": PrintAllContactsCommand(),
    "printnotes": PrintAllNotesCommand(),
    "printnoteswithtags": PrintNotesWithTagsCommand(),
    "getnotesbytag": GetNotesByTagCommand(),
}


record_args = set([e for c in commands.values() for a in c.get_args() for e in a])


def completer(text, state):
    options = []

    if text.startswith("--") or text.startswith("-"):
        options = [i for i in record_args if i.startswith(text)]
    else:
        options = [i for i in commands.keys() if i.startswith(text)]

    try:
        return options[state]
    except IndexError:
        return None


gnureadline.set_completer(completer)
gnureadline.parse_and_bind("tab: complete")


def split_arguments(input_string):
    args = re.findall(
        r"(?:--[a-zA-Z-]+|-{1,2}[a-zA-Z]+|[^\s-]+(?:\s+[^\s-]+)*)", input_string
    )

    return args


def execute_console():
    address_book = AddressBook(
        storage=Storage(BINARY_STORAGE_FILENAME),
    )
    note_book = NoteBook(
        storage=Storage(BINARY_NOTEBOOK_STORAGE_FILENAME),
    )

    while True:
        user_input = split_arguments(input("Enter a command: "))
        command = user_input[0].strip().lower()
        args = user_input[1:]

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command in ["help"]:
            print(
                "Currently supported commands are: \n"
                + "\n".join([str(k) for k in commands.keys()])
                + "\n"
                + "\n".join(["close", "exit", "help"])
                + "\nRun [command name] -h or [command name] --help for detailed usage"
            )

        elif command in commands:
            response = commands[command].executor(address_book, note_book, args)
            if response is not None:
                print(response)

        else:
            print("Invalid command.")
if __name__ == "__main__":
    execute_console()


#from datasources import ContactDto, ContactsDatasource
#
#cs = ContactsDatasource()
# cs.add_contact(ContactDto(
#     name='Serhii',
#     phones=['1234567891', '5263417896', '5465465464654'],
#     email='serhii@emailcom',
#     address='Ukraine, asdasd asda sdk ka n sljdnals ndalks ndlk',
#     birthday='26.11.1989',
# ))
# cs.add_contact(ContactDto(
#     name='Serhii 2',
#     phones=['6378378378', '7837837837', '3783783783783'],
#     email='serhii2@emailcom',
#     address='Ukraine, asdasd asda sdk ka n sljdnals ndalks ndlk',
#     birthday='12.05.2000',
# ))
# cs.add_contact(ContactDto(
#     name='Dmitro',
#     phones=['13516844554'],
#     email='serhii2@emailcom',
#     address='Ukraine, asdasd asda sdk ka n sljdnals ndalks ndlk',
#     birthday='12.05.2000',
# ))
#
#res = cs.search_contacts(name='serh')
#res2 = cs.search_contacts(birthday='26.11.1989')
#res3 = cs.search_contacts(birthday='26.11.1989', name='Serhiy')
#qwe = cs.delete_contact(name='Serhii 2')
#print(f'{len(res)} {len(res2)} {len(res3)}')