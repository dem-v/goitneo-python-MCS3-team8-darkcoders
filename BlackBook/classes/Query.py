class QueryField:
    def __init__(self, value, full_match=True, case_sensitive=True):
        self.value = value
        self.full_match = full_match
        self.case_sensitive = case_sensitive

class Query:
    def __init__(self, name, phone=None, email=None, address=None, birthday=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.birthday = birthday

