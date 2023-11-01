num = int(input("Enter a number: "))

is_even = True

while num > 0:
    num -= 2
    if num == 0:
        is_even = True
        break
    elif num < 0:
        break

if is_even:
    print("The number is even.")
else: 
    print("The number is odd.")