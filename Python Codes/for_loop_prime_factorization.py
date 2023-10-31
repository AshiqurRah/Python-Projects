def prime_factorization(number):
    factors = []

    while number % 2 == 0:
        factors.append(2)
        number //=2

    for i in range(2, int(number**0.5) + 1, 2):
        while number % i == 0:
            factors.append(i)
            number //= i

    if number > 2:
        factors.append(number)

    return factors

number = int(input("Enter a number: "))

result = prime_factorization(number)
print(f"The prime factorization of {number} is: {result}")