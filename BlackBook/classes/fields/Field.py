
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
