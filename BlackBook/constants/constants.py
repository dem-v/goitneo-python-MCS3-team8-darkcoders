from datetime import datetime

MAX_DELTA_DAYS = 7
WEEKDAYS_LIST = [datetime(year=2001, month=1, day=i).strftime('%A') for i in range(1,8)]
BINARY_STORAGE_FILENAME = 'dump.pickle'