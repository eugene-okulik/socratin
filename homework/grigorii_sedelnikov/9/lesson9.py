# date

import datetime

string_date = "Jan 15, 2023 - 12:05:33"
date_python = datetime.datetime.strptime(string_date, "%b %d, %Y - %H:%M:%S")
print(date_python.strftime("%B"))
print(date_python.strftime("%d.%m.%Y, %H:%M"))

# Map, filter
temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]
warm_days = list(filter(lambda x: x > 28, temperatures))

print(f"Максмиальная температура {max(warm_days)}")
print(f"Минимальная температура {min(warm_days)}")
print(f"Средняя температура {round(sum(warm_days) / len(warm_days))}")
