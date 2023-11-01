from .exception_handling import ValidationException
from datetime import datetime
import re


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self._value)

    def __eq__(self, other):
        if isinstance(other, Field):
            return self._value == other._value
        return False

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = self.validate(v)

    def validate(self, v):
        return v

    def check(self, query_field):
        # This base method should be overridden in subclasses
        raise NotImplementedError("Subclasses should implement this method.")


class StringValueField(Field):

    def matches_query(self, query_field):
        if query_field is not None:
            if query_field.full_match:
                if query_field.case_sensitive:
                    return self.value == query_field.value
                else:
                    return self.value.lower() == query_field.value.lower()
            else:
                if query_field.case_sensitive:
                    return query_field.value in self.value
                else:
                    return query_field.value.lower() in self.value.lower()
        return True


class NameField(StringValueField):

    def validate(self, value):
        if value == None:
            raise ValidationException(
                message="Name is required"
            )

        if len(value) <= 2:
            raise ValidationException(
                message="Name must be longer than 2 symbols"
            )

        return value


class PhoneField(StringValueField):
    def validate(self, value):
        phone_pattern = r'^\d{10}$'
        if not re.match(phone_pattern, value):
            raise ValidationException("Invalid phone number format")

        return value


class EmailField(StringValueField):
    def validate(self, value):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, value):
            raise ValidationException("Invalid email address format")

        return value


class AddressField(StringValueField):
    def validate(self, value):
        return value


class BirthdayField(Field):

    def validate(self, value):
        try:
            if isinstance(value, str):
                return datetime.strptime(value, '%d.%m.%Y')
            elif isinstance(value, datetime):
                return value
            else:
                raise ValidationException("Invalid birthday format")
        except ValueError:
            raise ValidationException("Invalid birthday format")


    def matches_query(self, query_field):
        if query_field is not None and isinstance(self.value, datetime):
            try:
                query_date = datetime.strptime(query_field.value, '%d.%m.%Y')
            except ValueError:
                return False

            birthday_date = self.value.date()

            if query_field.full_match:
                return birthday_date == query_date.date() or birthday_date == query_date.date().casefold()

            else:
                query_date_str = query_date.strftime('%Y-%m-%d')
                birthday_date_str = birthday_date.strftime('%Y-%m-%d')

                if query_field.case_sensitive:
                    return query_date_str in birthday_date_str
                else:
                    return query_date_str.casefold() in birthday_date_str.casefold()

        return True
