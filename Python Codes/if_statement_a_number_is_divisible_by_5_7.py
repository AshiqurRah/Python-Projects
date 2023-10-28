num = int(input("Enter a number: "))

if (num % 5 == 0) and (num % 7 == 0):
    print(f"{num} is divisible by both 5 and 7.")
else:
    print(f"{num} is not divisible by both 5 and 7.")