from .Field import Field


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
