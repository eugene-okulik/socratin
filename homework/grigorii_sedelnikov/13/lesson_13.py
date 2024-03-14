import calendar
from datetime import datetime, timedelta
import os

base_path = os.path.dirname(__file__)
target_path = os.path.join(os.path.dirname(os.path.dirname(base_path)), 'eugene_okulik', 'hw_13', 'data.txt')

with open(target_path, 'r') as f:
    text = f.readlines()


def get_date(string):
    return datetime.strptime(string[3:29], '%Y-%m-%d %H:%M:%S.%f')


data1_result = get_date(text[0]) + timedelta(days=7)
print(data1_result)

data2_result = get_date(text[1]).weekday()
print(calendar.day_name[data2_result])

data3_result = datetime.now() - get_date(text[2])

print(data3_result.days)
