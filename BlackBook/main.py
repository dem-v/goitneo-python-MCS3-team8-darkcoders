import pickle
from constants import BINARY_STORAGE_FILENAME
from actions import OPERATIONS, parse_input, DEFAULT_METHOD
from classes import AddressBook


def execute_console():
    try:
        with open(BINARY_STORAGE_FILENAME, 'rb') as fh:
            book = pickle.load(fh) 
        print("Loaded previous address book")
    except Exception as e:
        print(f"Previous address book could not be loaded. {e} \nInitializing new one.")
        book = AddressBook()
        
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        print(
            OPERATIONS[command, DEFAULT_METHOD](book, args)
        )
        if command in ["close", "exit"]:
            break
        
    retry = True
    while retry:
        retry = False
        try:
            with open(BINARY_STORAGE_FILENAME, 'wb') as fh:
                pickle.dump(book, fh)
            print("The address book was saved")
        except Exception as e:
            print(f"The address book could not be saved. Error: {e}")
            a = input("Would you like to retry? (y/n, default n)")
            if a == 'y' or a[0] == 'y':
                retry = True


if __name__ == "__main__":
    execute_console()
