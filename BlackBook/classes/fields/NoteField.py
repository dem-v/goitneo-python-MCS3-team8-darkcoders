from .StringValueField import StringValueField


class NoteField(StringValueField):
    def validate(self, value):
        return value
