from .Field import Field

class Name(Field):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return str(self.value) == str(other.value)