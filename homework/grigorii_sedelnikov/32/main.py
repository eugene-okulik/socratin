import time, requests

import requests

while True:
    time.sleep(2)
    print("Прошла 1 минута")
    requests.get("https://www.google.com")
    print("Запрос отправлен")