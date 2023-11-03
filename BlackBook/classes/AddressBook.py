from datetime import datetime
from collections import defaultdict, UserDict
from .Record import Record
from .Storage import Storage
from .exception_handling import KeyExistInContacts
from .query.Query import Query


def _save_to_disk_decorator(method):
    def wrapper(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        self.storage.save_to_disk(self.data)
        return result

    return wrapper


class AddressBook(UserDict):
    def __init__(self, storage: Storage):
        self.storage = storage
        self.data = storage.read_from_disk()
        print(self.print_all_contacts())

    def find(self, name: str):
        if name not in self.data.keys():
            return None
        else:
            return self.data.get(name)

    def delete(self, name: str):
        if name in self.data.keys():
            _ = self.data.pop(name)

    def get_birthdays_per_week(self, MAX_DELTA_DAYS, WEEKDAYS_LIST) -> str:
        user_bd_by_weekday = defaultdict(list)
        current_date = datetime.today().date()
        for name, user in self.data.items():
            if user.birthday is None:
                continue

            birthday = user.birthday.value.date()
            birthday_this_year = birthday.replace(year=current_date.year)

            today_distance = (birthday_this_year - current_date).days
            # let's not forget about those who had birthday on weekend and today is Monday
            if today_distance < 0:
                today_distance = (
                    birthday_this_year.replace(year=current_date.year + 1)
                    - current_date
                ).days
                if today_distance > MAX_DELTA_DAYS:
                    continue

            if today_distance > MAX_DELTA_DAYS:
                continue

            bd_week_day = birthday_this_year.weekday()

            if (bd_week_day == 5 and today_distance < MAX_DELTA_DAYS - 2) or (
                bd_week_day == 6 and today_distance < MAX_DELTA_DAYS - 1
            ):
                bd_week_day = 0

            bd_week_day_name = WEEKDAYS_LIST[bd_week_day]

            user_bd_by_weekday[bd_week_day_name].append(name)

        return "".join(
            [
                "{}: {}\n".format(d, user_bd_by_weekday[d])
                for d in user_bd_by_weekday
                if len(user_bd_by_weekday[d]) > 0
            ]
        )

    @_save_to_disk_decorator
    def add_record(self, rec: Record):
        if self.data.get(rec.name.value) is not None:
            raise KeyExistInContacts()

        self.data[rec.name.value] = rec

    def search_records(self, query: Query):
        matching_records = []
        for record in self.data.values():
            if record.matches_query(query):
                matching_records.append(record)
        return matching_records

    @_save_to_disk_decorator
    def edit_records(self, query: Query, **kwargs):
        updated_count = 0
        for record in self.search_records(query):
            record.update(**kwargs)  # Update fields
            updated_count += 1
        # Save to disk after editing
        return updated_count

    @_save_to_disk_decorator
    def remove_records(self, query: Query):
        removed_count = 0
        for record in self.search_records(query):
            del self.data[record.name.value]
            removed_count += 1
        return removed_count

    def print_all_contacts(self):
        return (
            "CONTACTS: \n\n"
            + "\n".join([f"{contact}" for contact in self.data.values()])
            + "\n"
        )
