import random

salary = int(input("Enter your salary: "))
bonus = input("Your bonus: ")
bonus_sum = random.randint(0, 100)

if bonus.lower() == "true":
    print(f"${round(salary+salary*bonus_sum/100)}")
else:
    print(f"${salary}")