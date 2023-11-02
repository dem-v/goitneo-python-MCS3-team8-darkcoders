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
)
from constants import BINARY_STORAGE_FILENAME, BINARY_NOTEBOOK_STORAGE_FILENAME
import re


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
}


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
