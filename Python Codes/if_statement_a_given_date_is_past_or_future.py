from datetime import datetime

current_date = datetime.now()

user_input = input("Enter a date (YYYY-MM-DD): ")

user_date = datetime.strptime(user_input, "%Y-%m-%d")
user_date

if user_date < current_date:
    print("The given date is in the past.")
elif user_date > current_date:
    print("The given date is in the future.")
else:
    print("The given date is today.")