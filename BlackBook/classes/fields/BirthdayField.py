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
        if not isinstance(self.value, datetime) or not query_field:
            return True

        if not query_field.value and query_field.daysAfterToday is None:
            return True

        if query_field.value:
            try:
                query_date = datetime.strptime(query_field.value, "%d.%m.%Y")
            except ValueError:
                return False
        else:
            query_date = datetime.now()

        if query_field.daysAfterToday is not None:
            query_date += timedelta(days=query_field.daysAfterToday)

        return self.value.date() == query_date.date()
