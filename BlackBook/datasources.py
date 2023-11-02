import sqlite3
from datetime import datetime

DATE_FORMAT = '%d.%m.%Y'


class ContactDto:
    def __init__(self, name, email=None, phones=None, address=None, birthday=None, id=None):
        self.id = id
        self.name = name
        self.email = email
        self.phones = phones
        self.address = address
        self.birthday = datetime.strptime(
            birthday, DATE_FORMAT) if birthday else None

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "phones": ','.join(self.phones if self.phones != None else []),
            "address": self.address,
            "birthday": self.birthday.strftime(DATE_FORMAT) if self.birthday else None
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name"),
            email=data.get("email"),
            phones=data.get('phones').split(
                ',') if data.get("phones") != None else [],
            address=data.get("address"),
            birthday=datetime.strptime(
                data.get("birthday"), DATE_FORMAT) if data.get("birthday") else None
        )


class NoteDto:
    def __init__(self, contact_id, note, tags=None, id=None):
        self.id = id
        self.contact_id = contact_id
        self.note = note
        self.tags = tags

    def to_dict(self):
        return {
            "contact_id": self.contact_id,
            "note": self.note,
            "tags": ','.join(self.tags if self.tags != None else []),
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            contact_id=data.get("contact_id"),
            note=data.get("note"),
            tags=data.get('tags').split(
                ',') if data.get("tags") != None else []
        )


class ContactsDatasource:
    def __init__(self):
        self.con = sqlite3.connect('database.db')
        self.__migrate__()

    def __migrate__(self):
        create_contact_table = """
        CREATE TABLE IF NOT EXISTS Contact (
            id INTEGER PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255),
            phones VARCHAR(255),
            address VARCHAR(255),
            birthday DATE,
            CONSTRAINT unique_name UNIQUE (name)
        );
        """

        cursor = self.con.cursor()
        cursor.execute(create_contact_table)
        cursor.close()

    def add_contact(self, contact: ContactDto):
        cursor = self.con.cursor()
        try:
            contact_dict = contact.to_dict()
            keys = contact_dict.keys()
            values = contact_dict.values()

            placeholders = ', '.join([f':{k}' for k in keys])
            query = f"INSERT INTO Contact ({', '.join(keys)}) VALUES ({placeholders})"

            cursor.execute(query, list(values))
            self.con.commit()
        finally:
            cursor.close()

    def edit_contact(self, contact: ContactDto):
        cursor = self.con.cursor()
        try:
            cursor.execute("SELECT id FROM Contact WHERE id=?", (contact.id,))
            existing_contact = cursor.fetchone()

            if existing_contact:
                contact_dict = contact.to_dict()
                keys = contact_dict.keys()
                values = contact_dict.values()

                set_clause = ', '.join([f"{k}=?" for k in keys])
                query = f"UPDATE Contact SET {set_clause} WHERE id=?"

                cursor.execute(query, tuple(values) + (contact.id,))
                self.con.commit()
                print("Contact edited successfully.")
            else:
                print("Contact does not exist. Cannot edit.")
        finally:
            cursor.close()

    def delete_contact(self, contact_id=None, name=None):
        cursor = self.con.cursor()
        try:
            existing_contact = None
            if contact_id is not None:
                cursor.execute(
                    "SELECT id FROM Contact WHERE id=?", (contact_id,))
                existing_contact = cursor.fetchone()
            elif name is not None:
                cursor.execute("SELECT id FROM Contact WHERE name=?", (name,))
                existing_contact = cursor.fetchone()

            if existing_contact:
                cursor.execute("DELETE FROM Contact WHERE id=?",
                               (existing_contact[0],))
                self.con.commit()
                print("Contact deleted successfully.")
            else:
                print("Contact does not exist. Cannot delete.")
        finally:
            cursor.close()

    def search_contacts(self, name=None, email=None, phones=None, address=None, birthday=None, partial_match=True, id=None):
        cursor = self.con.cursor()
        try:
            conditions = []
            values = []

            if id != None:
                conditions.append("id = ?")
                values.append(id)
            else:
                if name:
                    if partial_match:
                        conditions.append("name LIKE ?")
                        values.append(f"%{name}%")
                    else:
                        conditions.append("name = ?")
                        values.append(name)

                if email:
                    if partial_match:
                        conditions.append("email LIKE ?")
                        values.append(f"%{email}%")
                    else:
                        conditions.append("email = ?")
                        values.append(email)

                if phones:
                    for phone in phones:
                        if partial_match:
                            conditions.append("phones LIKE ?")
                            values.append(f"%{phone}%")
                        else:
                            conditions.append("phones = ?")
                            values.append(phone)

                if address:
                    if partial_match:
                        conditions.append("address LIKE ?")
                        values.append(f"%{address}%")
                    else:
                        conditions.append("address = ?")
                        values.append(address)

                if birthday:
                    conditions.append("birthday = ?")
                    values.append(birthday)

                if conditions:
                    query_str = "SELECT * FROM Contact WHERE " + \
                        " AND ".join(conditions)
                    cursor.execute(query_str, tuple(values))
                else:
                    cursor.execute("SELECT * FROM Contact")

            results = cursor.fetchall()
            contacts = []

            for row in results:
                contact = ContactDto(
                    id=row[0],
                    name=row[1],
                    email=row[2],
                    phones=row[3].split(',') if row[3] else [],
                    address=row[4],
                    birthday=row[5]
                )
                contacts.append(contact)

            return contacts
        finally:
            cursor.close()


class NotesDatasource:
    def __init__(self):
        self.con = sqlite3.connect('database.db')
        self.__migrate__()

    def __migrate__(self):
        create_note_table = """
        CREATE TABLE IF NOT EXISTS Note (
            id INTEGER PRIMARY KEY,
            contact_id INTEGER,
            note TEXT NOT NULL,
            tags VARCHAR(255),
            FOREIGN KEY (contact_id) REFERENCES Contact(id)
        );
        """

        cursor = self.con.cursor()
        cursor.execute(create_note_table)
        cursor.close()

    def add_note(self, note: NoteDto):
        cursor = self.con.cursor()
        try:
            cursor.execute(
                "SELECT id FROM Contact WHERE id=?",
                (note.contact_id,)
            )
            existing_contact = cursor.fetchone()

            if existing_contact:
                note_dict = note.to_dict()
                keys = note_dict.keys()
                values = note_dict.values()

                placeholders = ', '.join(['?' for _ in keys])
                query = f"INSERT INTO Note ({', '.join(keys)}) VALUES ({placeholders})"

                cursor.execute(query, tuple(values))
                self.con.commit()
                print("Note added successfully.")
            else:
                print("Contact does not exist. Cannot add the note.")
        finally:
            cursor.close()

    def edit_note(self, note: NoteDto):
        cursor = self.con.cursor()
        try:
            cursor.execute("SELECT id FROM Note WHERE id=?", (note.id,))
            existing_note = cursor.fetchone()

            if existing_note:
                note_dict = note.to_dict()
                keys = note_dict.keys()
                values = note_dict.values()

                set_clause = ', '.join([f"{k}=?" for k in keys])
                query = f"UPDATE Note SET {set_clause} WHERE id=?"

                cursor.execute(query, tuple(values) + (note.id,))
                self.con.commit()
                print("Note edited successfully.")
            else:
                print("Note does not exist. Cannot edit.")
        finally:
            cursor.close()

    def find_notes(self, id=None, note=None, tags=None, contact_id=None, partial_match=True):
        cursor = self.con.cursor()

        conditions = []
        values = []

        if id is not None:
            conditions.append("id = ?")
            values.append(id)
        else:
            if contact_id != None:
                conditions.append("contact_id = ?")
                values.append(contact_id)    
            if note is not None:
                if partial_match:
                    conditions.append("note LIKE ?")
                    values.append(f"%{note}%")
                else:
                    conditions.append("note = ?")
                    values.append(note)
            if tags is not None:
                if partial_match:
                    conditions.append("tags LIKE ?")
                    values.append(f"%{tags}%")
                else:
                    conditions.append("tags = ?")
                    values.append(tags)

        query = "SELECT * FROM Note"

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        cursor.execute(query, tuple(values))
        results = cursor.fetchall()
        cursor.close()

        notes = []
        for row in results:
            note = NoteDto(
                id=row[0],
                contact_id=row[1],
                note=row[2],
                tags=row[3]
            )
            notes.append(note)

        return notes
