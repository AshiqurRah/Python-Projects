print("///Welcome to Rollercoaster Ride///")
height = int(input("What is you hieght in cm? \n"))
bill = 0
if height >= 120:
    print("You can ride Rollercoaster")
    age = int(input("What is you age?\n"))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")
else:
    print("Sorry, you are not eligible for a ride. ")








