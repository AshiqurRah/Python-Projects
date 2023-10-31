n = int(input("Enter the numer of Fibonacci numbers to generate: "))

fibonacci = [0, 1]

for i in range(2, n):
    next_number = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_number)

print("Fibonacci Sequence:")
for num in fibonacci:
    print(num, end=", ")