print("///Welcome to Leap Year Finding Calculator///")
year = int(input("Which year would you like to check?\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Yes, this year is a leap year.")
        else:
            print("Sorry, this year is not a leap year.")
    else:
        print("Yes, this year is a leap year.")
else:
    print("Sorry, this year is not a leap year.")
