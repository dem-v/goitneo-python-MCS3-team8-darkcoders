from .StringValueField import StringValueField


class NoteField(StringValueField):
    def __init__(self, text, tags=None):
        super().__init__(text)
        self.tags = tags if tags is not None else []

    def validate(self, value):
        return value

    def add_tag(self, tag):
        self.tags.append(tag)

    def remove_tag(self, tag):
        self.tags.remove(tag)

    def __str__(self):
        return f"{self.value} Tags: {', '.join(self.tags)}"
