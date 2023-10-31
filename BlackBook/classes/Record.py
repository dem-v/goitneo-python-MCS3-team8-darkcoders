from .exception_handling import input_error, PhoneNumberIsMissing, BadBirthdayFormat
from .Name import Name
from .Phone import Phone
from .Birthday import Birthday

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}{f', birthday {self.show_birthday()}' if self.birthday is not None else ''}"

    def __eq__(self, __value: object) -> bool:
        return self.name == __value.name and not bool(
            set(self.phones).intersection(__value.phones)
        )

    @input_error
    def add_phone(self, phone: str):
        p = Phone(phone)
        self.phones.append(p)

    @input_error
    def edit_phone(self, orig_phone: str, new_phone: str):
        a = Phone(orig_phone)
        b = Phone(new_phone)

        try:
            ind = self.phones.index(a)
        except ValueError:
            raise PhoneNumberIsMissing(orig_phone)

        self.phones[ind] = b

    @input_error
    def remove_phone(self, phone: str):
        p = Phone(phone)
        self.phones.remove(p)

    @input_error
    def find_phone(self, phone: str):
        p = Phone(phone)
        return p if p in self.phones else None
    
    @input_error
    def add_birthday(self, value):
        try:
            self.birthday = Birthday(value)
        except ValueError:
            raise BadBirthdayFormat(value)
        
    def show_birthday(self):
        return str(self.birthday)