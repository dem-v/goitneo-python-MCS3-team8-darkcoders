from .StringValueField import StringValueField
from ..exception_handling import ValidationException


class NameField(StringValueField):
    def validate(self, value):
        if value is None:
            raise ValidationException(message="Name is required")

        if len(value) <= 2:
            raise ValidationException(message="Name must be longer than 2 symbols")

        return value
