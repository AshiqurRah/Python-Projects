n_terms = int(input("Enter the number of fibonacci terms: "))

term1, term2 = 0, 1

count = 0

if n_terms <=0:
    print("Please enter a positive number of terms.")
else:
    print("Fibonacci Sequence:")
    while count < n_terms:
        print(term1, end = " ")
        next_term = term1 + term2
        term1 = term2
        term2 = next_term
        count += 1
