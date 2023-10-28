def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_sum_of_two_primes(number):
    if number <= 1:
        return False
    
    for i in range(2, number // 2 + 1):
        if is_prime(i) and is_prime(number - i):
            return True
    return False

number_to_check = int(input("Enter a number: "))

if is_sum_of_two_primes(number_to_check):
    print(f"{number_to_check} is the sum of two prime numbers.")
else:
    print(f"{number_to_check} is not the sum of tw prime numbers.")