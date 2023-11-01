num = int(input("Enter an inteer: "))

digit_sum = 0
temp_num = abs(num)

while temp_num > 0:
    digit = temp_num % 10
    digit_sum += digit
    temp_num //= 10

print(f"The sum of the digits of {num} is {digit_sum}")