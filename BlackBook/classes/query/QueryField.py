class QueryField:
    def __init__(self, value, full_match=True, case_sensitive=True):
        self.value = value
        self.full_match = full_match
        self.case_sensitive = case_sensitive
