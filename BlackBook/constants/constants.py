from datetime import datetime

MAX_DELTA_DAYS = 7
WEEKDAYS_LIST = [
    datetime(year=2001, month=1, day=i).strftime("%A") for i in range(1, 8)
]
BINARY_STORAGE_FILENAME = "abook"
BINARY_NOTEBOOK_STORAGE_FILENAME = "notes"

COMMANDS = ['add', 'change', 'phone', 'show all', 'add-birthday',
            'show-birthday', 'birthdays', 'add-note', 'edit-note',
            'remove-note', 'get-notes', 'close', 'exit', 'hello', 'help']
RECORD_ARGS = ['--name', '--email', '--phones', '--birthday', '--address']
