from .StringValueField import StringValueField
from ..exception_handling import ValidationException


class AddressField(StringValueField):
    def validate(self, value):
        return value
