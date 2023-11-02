from .Field import Field
from ..exception_handling import ValidationException
from datetime import datetime


class BirthdayField(Field):
    def validate(self, value):
        try:
            if isinstance(value, str):
                return datetime.strptime(value, "%d.%m.%Y")
            elif isinstance(value, datetime):
                return value
            else:
                raise ValidationException("Invalid birthday format")
        except ValueError:
            raise ValidationException("Invalid birthday format")

    def matches_query(self, query_field):
        if query_field is not None and isinstance(self.value, datetime):
            try:
                query_date = datetime.strptime(query_field.value, "%d.%m.%Y")
            except ValueError:
                return False

            birthday_date = self.value.date()

            if query_field.full_match:
                return (
                    birthday_date == query_date.date()
                    or birthday_date == query_date.date().casefold()
                )

            else:
                query_date_str = query_date.strftime("%Y-%m-%d")
                birthday_date_str = birthday_date.strftime("%Y-%m-%d")

                if query_field.case_sensitive:
                    return query_date_str in birthday_date_str
                else:
                    return query_date_str.casefold() in birthday_date_str.casefold()

        return True
