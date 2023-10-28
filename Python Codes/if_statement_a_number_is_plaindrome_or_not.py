number = int(input("Enter a number: "))

reversed_number = 0
original_number = number

while number > 0:
    remainder = number % 10
    reversed_number = reversed_number * 10 + remainder
    number = number // 10

if original_number == reversed_number:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")