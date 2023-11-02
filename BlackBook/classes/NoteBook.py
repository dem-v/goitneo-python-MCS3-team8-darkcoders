from collections import UserList
from .Storage import Storage
from .fields.NoteField import NoteField
from .exception_handling import input_error, NoteNotFound


def _save_to_disk_decorator(method):
    def wrapper(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        self.storage.save_to_disk(self.data)
        return result

    return wrapper


class NoteBook(UserList):
    def __init__(self, storage: Storage):
        self.storage = storage
        self.data = storage.read_from_disk()
        for d in self.data:
            print(f"{d}")

    @_save_to_disk_decorator
    def add_record(self, rec: NoteField):
        self.data.append(rec)

    def search_records(self, query: str):
        matching_records = {}
        for index, record in enumerate(self.data):
            if query in record.value or query in record.tags:
                matching_records[index] = record
        return matching_records

    @_save_to_disk_decorator
    def edit_record(self, rec_id: int, new_value: NoteField):
        if 0 <= rec_id < len(self.data):
            self.data[rec_id] = new_value
        else:

            def throw_bad_note_index(id: int):
                raise NoteNotFound(f"Note index {id} out of range.")

            input_error(throw_bad_note_index)

    @_save_to_disk_decorator
    def remove_record(self, rec_id: int):
        if 0 <= rec_id < len(self.data):
            return self.data.pop(rec_id)
        else:

            def throw_bad_note_index(id: int):
                raise NoteNotFound(f"Note index {id} out of range.")

            input_error(throw_bad_note_index, id)
