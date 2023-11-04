class Query:
    def __init__(self, name, phone=None, email=None, address=None, birthday=None, birthdayAfter=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.birthday = birthday
        self.birthdayAfter = birthdayAfter
