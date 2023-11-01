from datetime import datetime
from collections import defaultdict, UserDict
from .Record import Record
from .Storage import Storage


def _save_to_disk_decorator(method):
    def wrapper(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        self.storage.safe_to_disk(self.data)
        return result

    return wrapper


class AddressBook(UserDict):
    def __init__(self, storage: Storage):
        self.storage = storage
        self.data = storage.read_from_disk()

    def find(self, name: str):
        if not name in self.data.keys():
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
                today_distance = (birthday_this_year.replace(
                    year=current_date.year + 1) - current_date).days
                if today_distance > MAX_DELTA_DAYS:
                    continue

            if today_distance > MAX_DELTA_DAYS:
                continue

            bd_week_day = birthday_this_year.weekday()

            if (bd_week_day == 5 and today_distance < MAX_DELTA_DAYS - 2) or (bd_week_day == 6 and today_distance < MAX_DELTA_DAYS - 1):
                bd_week_day = 0

            bd_week_day_name = WEEKDAYS_LIST[bd_week_day]

            user_bd_by_weekday[bd_week_day_name].append(name)

        return ''.join(['{}: {}\n'.format(d, user_bd_by_weekday[d]) for d in user_bd_by_weekday if len(user_bd_by_weekday[d]) > 0])

    def search_records(self, query):
        return self.data.values()

    @_save_to_disk_decorator
    def add_record(self, rec: Record):
        self.data[rec.name.value] = rec

    @_save_to_disk_decorator
    def edit_records(self, query, name=None, phone=None, email=None, address=None, birthday=None):
        updated_count = 0
        for record in self.search_records(query):
            r = self.data[record.name.value]
            updated_count += 1
            # if r != None:
            #     if fields.name != None:
            #         record.name = fields.name
            #     if fields.email != None:
            #         record.email = fields.email
            #     if fields.address != None:
            #         record.address = fields.address
            #     if fields.birthday != None:
            #         record.birthday = fields.birthday
            #     if fields.phone != None:
            #         record.phone.append(fields.phone)
        return updated_count

    @_save_to_disk_decorator
    def remove_records(self, query):
        removed = 0
        for record in self.search_records(query):
            removed += 1

        return removed
