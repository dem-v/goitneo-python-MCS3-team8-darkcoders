from datetime import datetime
from collections import defaultdict, UserDict
from .Record import Record

class AddressBook(UserDict):
    def add_record(self, rec: Record):
        self.data[str(rec.name)] = rec

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
            #let's not forget about those who had birthday on weekend and today is Monday
            if today_distance < 0:
                today_distance = (birthday_this_year.replace(year=current_date.year + 1) - current_date).days
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