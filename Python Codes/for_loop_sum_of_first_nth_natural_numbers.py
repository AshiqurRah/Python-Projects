n = int(input("Enter a positive integer n: "))

sum_of_natural_numbers = 0

for i in range(1, n+1):
    sum_of_natural_numbers += i

print(f"The sum of the first {n} natural numbers s {sum_of_natural_numbers}")