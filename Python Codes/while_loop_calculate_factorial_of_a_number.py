num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    while num > 0:
        factorial *= num
        num -=1


    print(f"The factorial is: {factorial}")