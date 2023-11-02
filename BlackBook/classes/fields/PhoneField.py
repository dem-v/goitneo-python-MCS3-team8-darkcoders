from .StringValueField import StringValueField
from ..exception_handling import ValidationException
import re


class PhoneField(StringValueField):
    def validate(self, value):
        phone_pattern = r"^\d{10}$"
        if not re.match(phone_pattern, value):
            raise ValidationException("Invalid phone number format")

        return value
