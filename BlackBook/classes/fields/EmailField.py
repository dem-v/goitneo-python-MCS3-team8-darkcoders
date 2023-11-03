from .StringValueField import StringValueField
from ..exception_handling import ValidationException
import re


class EmailField(StringValueField):
    def validate(self, value):
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(email_pattern, value):
            raise ValidationException("Invalid email address format")

        return value
