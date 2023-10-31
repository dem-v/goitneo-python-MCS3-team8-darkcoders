from .Field import Field
from .exception_handling import BadPhoneNumber

class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isnumeric():
            self.value = value
        else:
            raise BadPhoneNumber(value)

    def __str__(self):
        return str(self.value)