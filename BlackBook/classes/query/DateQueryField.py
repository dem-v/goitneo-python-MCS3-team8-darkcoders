from .QueryField import QueryField


class DateQueryField(QueryField):
    def __init__(self, value, full_match=True, case_sensitive=True, daysAfterToday=None):
        super().__init__(value, full_match=full_match, case_sensitive=case_sensitive)
        try:
            self.daysAfterToday = int(daysAfterToday) if daysAfterToday is not None else None
        except ValueError:
            self.daysAfterToday = None
