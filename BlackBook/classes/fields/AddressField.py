from .StringValueField import StringValueField


class AddressField(StringValueField):
    def validate(self, value):
        return value
