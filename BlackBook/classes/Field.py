class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if isinstance(other, Field):
            return self.value == other.value
        return False

    def check(self, query):
        # This base method should be overridden in subclasses
        raise NotImplementedError("Subclasses should implement this method.")

    def check_string(self, query):
        # Common string comparison logic
        if not query.case_sensitive:
            return (self.value.lower() == query.value.lower()) if query.full_match else (query.value.lower() in self.value.lower())
        else:
            return (self.value == query.value) if query.full_match else (query.value in self.value)


class NameField(Field):
    def check(self, query):
        return self.check_string(query)


class PhoneField(Field):
    def check(self, query):
        return self.check_string(query)


class EmailField(Field):
    def check(self, query):
        return self.check_string(query)


class AddressField(Field):
    def check(self, query):
        return self.check_string(query)


class BirthdayField(Field):
    def check(self, query):
        try:
            query_date = datetime.strptime(query.value, '%Y-%m-%d')
            return self.value == query_date
        except ValueError:
            return False
