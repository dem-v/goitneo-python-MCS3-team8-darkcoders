from .exception_handling import input_error, PhoneNumberIsMissing, BadBirthdayFormat, NoteExists, NoteNotFound
from .fields.NameField import NameField
from .fields.PhoneField import PhoneField
from .fields.EmailField import EmailField
from .fields.AddressField import AddressField
from .fields.BirthdayField import BirthdayField


class Record:
    def __init__(self, name, phones=[], email=None, address=None, birthday=None):
        self.name = NameField(name)
        self.phones = [PhoneField(phone) for phone in phones]
        self.email = EmailField(email) if email != None else None
        self.address = AddressField(address) if address != None else None
        self.birthday = BirthdayField(birthday) if birthday != None else None
        self.notes = []

    def __str__(self):
        fields = {
            "Name": self.name.value,
            "Phones": ", ".join(p.value for p in self.phones) if self.phones else None,
            "Email": self.email.value if self.email else None,
            "Address": self.address.value if self.address else None,
            "Birthday": self.birthday.value.strftime('%Y-%m-%d') if self.birthday else None
        }

        formatted_fields = [
            f'{field}: {value}' for field, value in fields.items() if value is not None
        ]

        return '\n'.join([
            'Contact Info:',
            *formatted_fields,
            ''
        ])

    def __eq__(self, __value: object) -> bool:
        return __value != None and self.name == __value.name and not bool(
            set(self.phones).intersection(__value.phones)
        )

    def update(self, **kwargs):
        fields = {k: v for k, v in kwargs.items() if v is not None}
        if 'name' in fields:
            self.name.value = fields['name']
        if 'phones' in fields and len(fields['phones']) > 0:
            self.phones = [PhoneField(p) for p in fields['phones']]
            print(self.phones)
        if 'email' in fields:
            if self.email is None:
                self.email = EmailField(fields['email'])
            else:
                self.email.value = fields['email']
        if 'address' in fields:
            if self.address is None:
                self.address = AddressField(fields['address'])
            else:
                self.address.value = fields['address']
        if 'birthday' in fields:
            if self.birthday is None:
                self.birthday = BirthdayField(fields['birthday'])
            else:
                self.birthday.value = fields['birthday']
        if 'replace_phone' in fields:
            replace_phone = fields['replace_phone']
            if len(replace_phone) > 0:
                found_index = next((index for index, phone in enumerate(
                    self.phones) if phone.value == replace_phone[0]), -1)
                if found_index >= 0:
                    if len(replace_phone) >= 2:
                        self.phones[found_index] = PhoneField(replace_phone[1])
                    else:
                        self.phones.pop(found_index)

    def matches_query(self, query):
        if query.name != None and self.name.matches_query(query_field=query.name):
            return True
        if query.phone is not None and any(phone_field.matches_query(query_field=query.phone) for phone_field in self.phones):
            return True
        if query.email != None and self.email != None and self.email.matches_query(query_field=query.email):
            return True
        if query.address != None and self.address != None and self.address.matches_query(query_field=query.address):
            return True
        if query.birthday != None and self.birthday != None and self.birthday.matches_query(query_field=query.birthday):
            return True

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

    @input_error
    def add_note(self, text):
        if any(note.text == text for note in self.notes):
            raise NoteExists(text)
        note = Note(text)
        self.notes.append(note)

    @input_error
    def edit_note(self, old_text, new_text):
        for note in self.notes:
            if note.text == old_text:
                note.text = new_text
                return
        raise NoteNotFound(old_text)

    @input_error
    def remove_note(self, text):
        self.notes = [note for note in self.notes if note.text != text]

    @input_error
    def get_notes(self):
        return [str(note) for note in self.notes]
