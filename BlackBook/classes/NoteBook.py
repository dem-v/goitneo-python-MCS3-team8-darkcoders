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
        data = storage.read_from_disk()
        self.data = data if isinstance(data, list) else list(data.values())
        print(self.print_all_notes())

    @_save_to_disk_decorator
    def add_record(self, rec: NoteField):
        if not isinstance(rec, NoteField):
            raise ValueError("Record must be an instance of NoteField")
        self.data.append(rec)

    def search_records(self, query: str):
        matching_records = {}
        for index, record in enumerate(self.data):
            if query in record.value:
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
        if 0 <= int(rec_id) < len(self.data):
            return self.data.pop(int(rec_id))
        else:

            def throw_bad_note_index(id: int):
                raise NoteNotFound(f"Note index {id} out of range.")

            input_error(throw_bad_note_index, int(rec_id))

    def print_all_notes(self):
        return (
            "NOTES: \n"
            + "\n".join(
                [f"{index}. {record}" for index, record in enumerate(self.data)]
            )
            + "\n"
        )

    def search_by_tag(self, tag):
        return {index: note for index, note in enumerate(self.data) if tag in note.tags}
