from .StringValueField import StringValueField


class NoteField(StringValueField):
    def __init__(self, text, tags=None):
        super().__init__(text)
        self.tags = tags or []

    def __str__(self):
        tag_string = ', '.join(self.tags)
        return f"{self.value} [Tags: {tag_string}]"

    def has_tag(self, tag):
        return tag in self.tags

    def validate(self, value):
        return value
