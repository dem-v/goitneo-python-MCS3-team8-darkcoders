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
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.completion import WordCompleter


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


argument_completer = WordCompleter(list(record_args), meta_dict=None, WORD=True)

command_completer = WordCompleter(list(commands.keys()), meta_dict=None, WORD=True)


print(f"DEBUG: record_args contents: {record_args}")


class CommandCompleter(Completer):
    def __init__(self, commands, record_args):
        self.commands = commands
        self.record_args = record_args

    def get_completions(self, document, complete_event):
        word_before_cursor = document.get_word_before_cursor(WORD=True)
        options = []

        if word_before_cursor.startswith("--") or word_before_cursor.startswith("-"):
            options = [i for i in record_args if i.startswith(word_before_cursor)]
        else:
            options = [i for i in commands.keys() if i.startswith(word_before_cursor)]

        for option in options:
            yield Completion(option, start_position=-len(word_before_cursor))


completer = CommandCompleter(commands, record_args)
session = PromptSession(completer=completer, history=InMemoryHistory())


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
        try:
            command_line = session.prompt("Enter a command: ")
        except KeyboardInterrupt:
            continue
        except EOFError:
            print("Good bye!")
            break

        user_input = split_arguments(command_line)
        if not user_input:
            continue
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
