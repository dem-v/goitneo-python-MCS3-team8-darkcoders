import pickle
from constants import BINARY_STORAGE_FILENAME
from actions import OPERATIONS, parse_input, DEFAULT_METHOD
from classes import AddressBook, NoteBook
from actions import *
import shlex
import re

# def execute_console():
#     try:
#         with open(BINARY_STORAGE_FILENAME, 'rb') as fh:
#             book = pickle.load(fh)
#         print("Loaded previous address book")
#     except Exception as e:
#         print(f"Previous address book could not be loaded. {e} \nInitializing new one.")
#         book = AddressBook()

#     print("Welcome to the assistant bot!")
#     while True:
#         user_input = input("Enter a command: ")
#         command, *args = parse_input(user_input)

#         print(
#             OPERATIONS[command, DEFAULT_METHOD](book, args)
#         )
#         if command in ["close", "exit"]:
#             break

#     retry = True
#     while retry:
#         retry = False
#         try:
#             with open(BINARY_STORAGE_FILENAME, 'wb') as fh:
#                 pickle.dump(book, fh)
#             print("The address book was saved")
#         except Exception as e:
#             print(f"The address book could not be saved. Error: {e}")
#             a = input("Would you like to retry? (y/n, default n)")
#             if a == 'y' or a[0] == 'y':
#                 retry = True

commands = {
    'add': AddContactCommand(),
    'delete': RemoveContactCommand(),
    'edit': EditContactCommand(),
    'search': SearchContactsCommand(),
}


def parse_parameters(input_string):
    pattern = r'(-\w+)\s+([^-\s][^-\n\r]*?)(?=\s+-\w+|$)'
    matches = re.finditer(pattern, input_string)

    arguments = []
    for match in matches:
        param = match.group(1).strip()
        value = match.group(2).strip()
        arguments.append(param)
        arguments.append(value)

    return arguments


def main():
    storage = Storage("records")
    asd = storage.read_from_disk()
    address_book = AddressBook(
        storage=storage,
    )
    note_book = NoteBook()

    while True:
        user_input = input("Enter a command: ").split(maxsplit=1)
        command = user_input[0].strip().lower()
        args = parse_parameters(''.join(user_input[1:]))

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command in commands:
            response = commands[command].executor(
                address_book,
                note_book,
                args
            )
            if response != None:
                if isinstance(response, list):
                    for s in response:
                        print(s)
                else:
                    print(response)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()


